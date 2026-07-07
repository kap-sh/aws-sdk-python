"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyTestCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id


class GetAutomatedReasoningPolicyTestCaseRequest(TypedDict, closed=True):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>"""
    test_case_id: "aws_sdk_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId"
    """<p>The unique identifier of the test to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyTestCaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyTestCaseRequest:
    out: GetAutomatedReasoningPolicyTestCaseRequest = {}  # type: ignore[typeddict-item]
    return out
