from deepeval import assert_test  # assert function
from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase  # Test case

from get_response import get_llm_response


def test_answer_relevancy():
    metric = AnswerRelevancyMetric(threshold=0.7)
    test_case = LLMTestCase(
        input="How do I reset my password?",
        actual_output=get_llm_response("How do I reset my password?"),
    )
    assert_test(test_case, [metric])
