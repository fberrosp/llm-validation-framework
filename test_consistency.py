from deepeval import assert_test  # assert function
from deepeval.test_case import LLMTestCase  # Test case
from deepeval.test_case import LLMTestCaseParams
from deepeval.metrics import GEval  # GEval -> LLM as a judge

from get_response import get_llm_response


def test_consistency():
    prompt = "Summarize the water cycle in one sentence."
    outputs = [get_llm_response(prompt) for _ in range(3)]  #

    for i, output in enumerate(outputs, 1):
        print(f"\n--- Output {i} ---")
        print(output)

    # Judge the consistency of the model's output using GEval
    consistency_metric = GEval(
        name='Consistency',
        criteria="Determine whether the three outputs are semantically consistent with one another. The outputs do not need to use the same wording or structure. They should convey the same core meaning and factual information. Minor differences in phrasing, detail, or sentence structure should not be considered inconsistent.",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
        threshold=0.7
    )

    # Combine outputs
    combined_outputs = "\n\n".join(
        f"Output {i+1}:\n{output}"
        for i, output in enumerate(outputs)
    )

    test_case = LLMTestCase(
        input=prompt,
        actual_output=combined_outputs
    )
    # Assert that the result is consistent
    assert_test(test_case, [consistency_metric])
