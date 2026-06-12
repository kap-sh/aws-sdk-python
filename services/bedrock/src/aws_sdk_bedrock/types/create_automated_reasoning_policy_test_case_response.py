"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateAutomatedReasoningPolicyTestCaseResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id


class CreateAutomatedReasoningPolicyTestCaseResponse(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the policy for which the test was created.</p>"""
    test_case_id: "aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId"
    """<p>The unique identifier of the created test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAutomatedReasoningPolicyTestCaseResponse) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["testCaseId"] = value["test_case_id"]
    return out


def deserialize_json(data: dict) -> CreateAutomatedReasoningPolicyTestCaseResponse:
    out: CreateAutomatedReasoningPolicyTestCaseResponse = {}  # type: ignore[typeddict-item]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyTestCaseResponse.policy_arn required"
        )
    if "testCaseId" in data:
        out["test_case_id"] = data["testCaseId"]
    else:
        raise DeserializationError(
            "CreateAutomatedReasoningPolicyTestCaseResponse.test_case_id required"
        )
    return out
