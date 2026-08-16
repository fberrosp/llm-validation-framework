from deepeval import assert_test
from deepeval.metrics import FaithfulnessMetric, ContextualPrecisionMetric, ContextualRecallMetric
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

from get_query import get_rag_query


def test_rag_pipeline():
    question = "What is the retirement plan policy?"
    answer, retrieved_context = get_rag_query(question)

    test_case = LLMTestCase(
        input=question,
        actual_output=answer,
        expected_output="The organization provides retirement plan for full time employees and part time employees who are 21 years or older. The organization contributes to the employees retirement plan after 1 year of employment. Employees may contribute to their plan at the start of their employment",
        retrieval_context=retrieved_context,
    )

    metrics = [
        FaithfulnessMetric(threshold=0.8),
        ContextualPrecisionMetric(threshold=0.7),
        ContextualRecallMetric(threshold=0.8),
        AnswerRelevancyMetric(threshold=0.8),
    ]
    assert_test(test_case, metrics)
