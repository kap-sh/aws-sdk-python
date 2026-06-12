"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyTestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_result

AutomatedReasoningPolicyTestList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_test_result.AutomatedReasoningPolicyTestResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyTestList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_test_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyTestList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_result

    out: AutomatedReasoningPolicyTestList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_test_result.deserialize_json(
                item
            )
        )
    return out
