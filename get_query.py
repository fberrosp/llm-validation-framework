from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from get_response import get_llm_response

loader = TextLoader("knowledge_base.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = splitter.split_documents(docs)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
vectorstore = Chroma.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever()


def get_rag_query(question: str):
    retrieved_docs = retriever.get_relevant_documents(question)
    context = "\n".join([d.page_content for d in retrieved_docs])
    prompt = f"Answer using only this context:\n{context}\n\nQuestion: {question}"
    answer = get_llm_response(prompt)
    return answer, [d.page_content for d in retrieved_docs]
