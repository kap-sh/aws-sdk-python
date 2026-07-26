"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicySourceDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_document_blob
    import capo_bedrock.types.automated_reasoning_policy_build_document_content_type
    import capo_bedrock.types.automated_reasoning_policy_build_document_description
    import capo_bedrock.types.automated_reasoning_policy_build_document_name
    import capo_bedrock.types.automated_reasoning_policy_document_sha256


class AutomatedReasoningPolicySourceDocument(TypedDict, closed=True):
    document: "capo_bedrock.types.automated_reasoning_policy_build_document_blob.AutomatedReasoningPolicyBuildDocumentBlob"
    """<p>The raw content of the source document as a binary blob.</p>"""
    document_content_type: "capo_bedrock.types.automated_reasoning_policy_build_document_content_type.AutomatedReasoningPolicyBuildDocumentContentType"
    """<p>The MIME type of the document (e.g., application/pdf, text/plain).</p>"""
    document_name: "capo_bedrock.types.automated_reasoning_policy_build_document_name.AutomatedReasoningPolicyBuildDocumentName"
    """<p>The name of the source document for identification purposes.</p>"""
    document_description: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_build_document_description.AutomatedReasoningPolicyBuildDocumentDescription"
    ]
    """<p>An optional description providing context about the document's content and purpose.</p>"""
    document_hash: "capo_bedrock.types.automated_reasoning_policy_document_sha256.AutomatedReasoningPolicyDocumentSha256"
    """<p>A SHA-256 hash of the document content, used for verification and integrity checking.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicySourceDocument) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_build_document_blob

    out["document"] = (
        capo_bedrock.types.automated_reasoning_policy_build_document_blob.serialize_json(
            value["document"]
        )
    )
    import capo_bedrock.types.automated_reasoning_policy_build_document_content_type

    out["documentContentType"] = (
        capo_bedrock.types.automated_reasoning_policy_build_document_content_type.serialize_json(
            value["document_content_type"]
        )
    )
    out["documentName"] = value["document_name"]
    if "document_description" in value:
        out["documentDescription"] = value["document_description"]
    out["documentHash"] = value["document_hash"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicySourceDocument:
    out: AutomatedReasoningPolicySourceDocument = {}  # type: ignore[typeddict-item]
    if "document" in data:
        import capo_bedrock.types.automated_reasoning_policy_build_document_blob

        out["document"] = (
            capo_bedrock.types.automated_reasoning_policy_build_document_blob.deserialize_json(
                data["document"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicySourceDocument.document required"
        )
    if "documentContentType" in data:
        import capo_bedrock.types.automated_reasoning_policy_build_document_content_type

        out["document_content_type"] = (
            capo_bedrock.types.automated_reasoning_policy_build_document_content_type.deserialize_json(
                data["documentContentType"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicySourceDocument.document_content_type required"
        )
    if "documentName" in data:
        out["document_name"] = data["documentName"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicySourceDocument.document_name required"
        )
    if "documentDescription" in data:
        out["document_description"] = data["documentDescription"]
    if "documentHash" in data:
        out["document_hash"] = data["documentHash"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicySourceDocument.document_hash required"
        )
    return out
