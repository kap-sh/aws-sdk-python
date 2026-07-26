"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_summary

AutomatedReasoningPolicyBuildWorkflowSummaries: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_build_workflow_summary.AutomatedReasoningPolicyBuildWorkflowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowSummaries) -> list:
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_workflow_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyBuildWorkflowSummaries:
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_summary

    out: AutomatedReasoningPolicyBuildWorkflowSummaries = []
    for item in data:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_workflow_summary.deserialize_json(
                item
            )
        )
    return out
