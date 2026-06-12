"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteAutomatedReasoningPolicyTestCaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id
    import aws_sdk_bedrock.types.timestamp


class DeleteAutomatedReasoningPolicyTestCaseRequest(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>"""
    test_case_id: "aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId"
    """<p>The unique identifier of the test to delete.</p>"""
    last_updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the test was last updated. This is used as a concurrency token to prevent conflicting modifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAutomatedReasoningPolicyTestCaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAutomatedReasoningPolicyTestCaseRequest:
    out: DeleteAutomatedReasoningPolicyTestCaseRequest = {}  # type: ignore[typeddict-item]
    return out
