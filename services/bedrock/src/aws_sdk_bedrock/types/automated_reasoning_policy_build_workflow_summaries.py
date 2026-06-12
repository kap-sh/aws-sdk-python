"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_summary

AutomatedReasoningPolicyBuildWorkflowSummaries: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_summary.AutomatedReasoningPolicyBuildWorkflowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowSummaries) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyBuildWorkflowSummaries:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_summary

    out: AutomatedReasoningPolicyBuildWorkflowSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_summary.deserialize_json(
                item
            )
        )
    return out
