"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyGenerateFidelityReportContent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list


class _AutomatedReasoningPolicyGenerateFidelityReportContent_documents(TypedDict):
    documents: "aws_sdk_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list.AutomatedReasoningPolicyGenerateFidelityReportDocumentList"


AutomatedReasoningPolicyGenerateFidelityReportContent: TypeAlias = (
    _AutomatedReasoningPolicyGenerateFidelityReportContent_documents
)


# --- restJson1 ser/de ---
def serialize_json(
    value: AutomatedReasoningPolicyGenerateFidelityReportContent,
) -> dict:
    if "documents" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list

        return {
            "documents": aws_sdk_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list.serialize_json(
                value["documents"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyGenerateFidelityReportContent: no variant present"
        )


def deserialize_json(
    data: dict,
) -> AutomatedReasoningPolicyGenerateFidelityReportContent:
    if "documents" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list

        return {
            "documents": aws_sdk_bedrock.types.automated_reasoning_policy_generate_fidelity_report_document_list.deserialize_json(
                data["documents"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyGenerateFidelityReportContent: no recognized variant key"
        )
