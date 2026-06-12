"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyIterativeRefinementDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_document

AutomatedReasoningPolicyIterativeRefinementDocumentList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_document.AutomatedReasoningPolicyBuildWorkflowDocument"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AutomatedReasoningPolicyIterativeRefinementDocumentList,
) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_document

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_document.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AutomatedReasoningPolicyIterativeRefinementDocumentList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_document

    out: AutomatedReasoningPolicyIterativeRefinementDocumentList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_document.deserialize_json(
                item
            )
        )
    return out
