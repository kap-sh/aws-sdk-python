"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyBuildWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id


class GetAutomatedReasoningPolicyBuildWorkflowRequest(TypedDict, closed=True):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to retrieve.</p>"""
    build_workflow_id: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyBuildWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyBuildWorkflowRequest:
    out: GetAutomatedReasoningPolicyBuildWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
