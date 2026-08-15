from deepeval import assert_test  # assert function
from deepeval.test_case import LLMTestCase  # Test case
from deepeval.test_case import LLMTestCaseParams
from deepeval.metrics import GEval  # GEval -> LLM as a judge

from get_response import get_llm_response


def test_correctness():

    # Judge the correctness of the model's output using GEval
    correctness_metric = GEval(
        name='Correctness',
        criteria='Determine if the model\'s output is factually correct based on the expected output.',
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT,
                           LLMTestCaseParams.EXPECTED_OUTPUT],
        threshold=0.7
    )

    # Define the test case
    test_case = LLMTestCase(
        input="What is the capital of France?",
        actual_output=get_llm_response("What is the capital of France?"),
        expected_output="Paris.",
    )

    # Assert that the result is correct
    assert_test(test_case, [correctness_metric])
