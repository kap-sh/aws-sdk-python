"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyAnnotationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_id


class GetAutomatedReasoningPolicyAnnotationsRequest(TypedDict, closed=True):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose annotations you want to retrieve.</p>"""
    build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow whose annotations you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedReasoningPolicyAnnotationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAutomatedReasoningPolicyAnnotationsRequest:
    out: GetAutomatedReasoningPolicyAnnotationsRequest = {}  # type: ignore[typeddict-item]
    return out
