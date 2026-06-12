"""Generated from Smithy shape ``com.amazonaws.bedrock#UpdateAutomatedReasoningPolicyTestCaseResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id


class UpdateAutomatedReasoningPolicyTestCaseResponse(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the policy that contains the updated test.</p>"""
    test_case_id: "aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId"
    """<p>The unique identifier of the updated test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomatedReasoningPolicyTestCaseResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["testCaseId"] = value["test_case_id"]
    return out


def deserialize_json(data: dict) -> UpdateAutomatedReasoningPolicyTestCaseResponse:
    out: UpdateAutomatedReasoningPolicyTestCaseResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyTestCaseResponse.policy_arn required"
        )
    if "testCaseId" in data:
        out["test_case_id"] = data["testCaseId"]
    else:
        raise DeserializationError(
            "UpdateAutomatedReasoningPolicyTestCaseResponse.test_case_id required"
        )
    return out
