"""Generated from Smithy shape ``com.amazonaws.bedrock#CancelAutomatedReasoningPolicyBuildWorkflowRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id


class CancelAutomatedReasoningPolicyBuildWorkflowRequest(TypedDict):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to cancel.</p>"""
    build_workflow_id: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow to cancel. You can get this ID from the StartAutomatedReasoningPolicyBuildWorkflow response or by listing build workflows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelAutomatedReasoningPolicyBuildWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelAutomatedReasoningPolicyBuildWorkflowRequest:
    out: CancelAutomatedReasoningPolicyBuildWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
