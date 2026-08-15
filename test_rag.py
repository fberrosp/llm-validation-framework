from deepeval import assert_test
from deepeval.metrics import FaithfulnessMetric, ContextualPrecisionMetric, ContextualRecallMetric
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

from get_query import get_rag_query


def test_rag_pipeline():
    question = "What is the paid sick leave policy?"
    answer, retrieved_context = get_rag_query(question)

    test_case = LLMTestCase(
        input=question,
        actual_output=answer,
        expected_output="Full time employees earn 7 hours per month beginning at the start of their employment. Unused hours can accumulate up to 210 hours for full time employees.",
        retrieval_context=retrieved_context,
    )

    metrics = [
        FaithfulnessMetric(threshold=0.8),
        ContextualPrecisionMetric(threshold=0.7),
        ContextualRecallMetric(threshold=0.8),
        AnswerRelevancyMetric(threshold=0.8),
    ]
    assert_test(test_case, metrics)
