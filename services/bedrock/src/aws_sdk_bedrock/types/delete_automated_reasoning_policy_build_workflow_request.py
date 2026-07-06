"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteAutomatedReasoningPolicyBuildWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_arn
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id
    import aws_sdk_bedrock.types.timestamp


class DeleteAutomatedReasoningPolicyBuildWorkflowRequest(TypedDict, closed=True):
    policy_arn: "aws_sdk_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to delete.</p>"""
    build_workflow_id: "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow to delete.</p>"""
    last_updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The timestamp when the build workflow was last updated. This is used for optimistic concurrency control to prevent accidental deletion of workflows that have been modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAutomatedReasoningPolicyBuildWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAutomatedReasoningPolicyBuildWorkflowRequest:
    out: DeleteAutomatedReasoningPolicyBuildWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
