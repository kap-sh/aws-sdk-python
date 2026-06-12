"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildWorkflowDocument``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_blob
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_description
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_name


class AutomatedReasoningPolicyBuildWorkflowDocument(TypedDict):
    document: "aws_sdk_bedrock.types.automated_reasoning_policy_build_document_blob.AutomatedReasoningPolicyBuildDocumentBlob"
    """<p>The actual content of the source document that will be analyzed to extract policy rules and concepts.</p>"""
    document_content_type: "aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type.AutomatedReasoningPolicyBuildDocumentContentType"
    """<p>The MIME type of the document content (e.g., text/plain, application/pdf, text/markdown).</p>"""
    document_name: "aws_sdk_bedrock.types.automated_reasoning_policy_build_document_name.AutomatedReasoningPolicyBuildDocumentName"
    """<p>A descriptive name for the document that helps identify its purpose and content.</p>"""
    document_description: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_policy_build_document_description.AutomatedReasoningPolicyBuildDocumentDescription"
    ]
    """<p>A detailed description of the document's content and how it should be used in the policy generation process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildWorkflowDocument) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_blob

    out["document"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_build_document_blob.serialize_json(
            value["document"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type

    out["documentContentType"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type.serialize_json(
            value["document_content_type"]
        )
    )
    out["documentName"] = value["document_name"]
    if "document_description" in value:
        out["documentDescription"] = value["document_description"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildWorkflowDocument:
    out: AutomatedReasoningPolicyBuildWorkflowDocument = {}  # type: ignore[typeddict-item]
    if "document" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_blob

        out["document"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_document_blob.deserialize_json(
                data["document"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildWorkflowDocument.document required"
        )
    if "documentContentType" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type

        out["document_content_type"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_document_content_type.deserialize_json(
                data["documentContentType"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildWorkflowDocument.document_content_type required"
        )
    if "documentName" in data:
        out["document_name"] = data["documentName"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildWorkflowDocument.document_name required"
        )
    if "documentDescription" in data:
        out["document_description"] = data["documentDescription"]
    return out
