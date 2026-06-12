"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyReportSourceDocumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document

AutomatedReasoningPolicyReportSourceDocumentList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document.AutomatedReasoningPolicyReportSourceDocument"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyReportSourceDocumentList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyReportSourceDocumentList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document

    out: AutomatedReasoningPolicyReportSourceDocumentList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_report_source_document.deserialize_json(
                item
            )
        )
    return out
