"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyGenerateFidelityReportDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_document

AutomatedReasoningPolicyGenerateFidelityReportDocumentList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_document.AutomatedReasoningPolicyBuildWorkflowDocument"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AutomatedReasoningPolicyGenerateFidelityReportDocumentList,
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
) -> AutomatedReasoningPolicyGenerateFidelityReportDocumentList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_document

    out: AutomatedReasoningPolicyGenerateFidelityReportDocumentList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_build_workflow_document.deserialize_json(
                item
            )
        )
    return out
