"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyGeneratedTestCases``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_case_list


class AutomatedReasoningPolicyGeneratedTestCases(TypedDict):
    generated_test_cases: "aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_case_list.AutomatedReasoningPolicyGeneratedTestCaseList"
    """<p>Represents a collection of generated test cases.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyGeneratedTestCases) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_case_list

    out["generatedTestCases"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_case_list.serialize_json(
            value["generated_test_cases"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyGeneratedTestCases:
    out: AutomatedReasoningPolicyGeneratedTestCases = {}  # type: ignore[typeddict-item]
    if "generatedTestCases" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_case_list

        out["generated_test_cases"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_generated_test_case_list.deserialize_json(
                data["generatedTestCases"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyGeneratedTestCases.generated_test_cases required"
        )
    return out
