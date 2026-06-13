"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyReportSourceDocument``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement_list
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_document_name
    import aws_sdk_bedrock.types.automated_reasoning_policy_document_id
    import aws_sdk_bedrock.types.automated_reasoning_policy_document_sha256


class AutomatedReasoningPolicyReportSourceDocument(TypedDict):
    document_name: "aws_sdk_bedrock.types.automated_reasoning_policy_build_document_name.AutomatedReasoningPolicyBuildDocumentName"
    """<p>The name of the source document that was analyzed.</p>"""
    document_hash: "aws_sdk_bedrock.types.automated_reasoning_policy_document_sha256.AutomatedReasoningPolicyDocumentSha256"
    """<p>A SHA-256 hash of the document content, used for verification and ensuring the document hasn't changed since analysis.</p>"""
    document_id: "aws_sdk_bedrock.types.automated_reasoning_policy_document_id.AutomatedReasoningPolicyDocumentId"
    """<p>A unique identifier for this document within the fidelity report.</p>"""
    atomic_statements: "aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement_list.AutomatedReasoningPolicyAtomicStatementList"
    """<p>The list of atomic statements extracted from this document, representing the fundamental units of meaning used for grounding.</p>"""
    document_content: "aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk_list.AutomatedReasoningPolicyAnnotatedChunkList"
    """<p>The document's content organized into annotated chunks with line number information for precise referencing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyReportSourceDocument) -> dict:
    out: dict = {}
    out["documentName"] = value["document_name"]
    out["documentHash"] = value["document_hash"]
    out["documentId"] = value["document_id"]
    import aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement_list

    out["atomicStatements"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement_list.serialize_json(
            value["atomic_statements"]
        )
    )
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk_list

    out["documentContent"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk_list.serialize_json(
            value["document_content"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyReportSourceDocument:
    out: AutomatedReasoningPolicyReportSourceDocument = {}  # type: ignore[typeddict-item]
    if "documentName" in data:
        out["document_name"] = data["documentName"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyReportSourceDocument.document_name required"
        )
    if "documentHash" in data:
        out["document_hash"] = data["documentHash"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyReportSourceDocument.document_hash required"
        )
    if "documentId" in data:
        out["document_id"] = data["documentId"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyReportSourceDocument.document_id required"
        )
    if "atomicStatements" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement_list

        out["atomic_statements"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_atomic_statement_list.deserialize_json(
                data["atomicStatements"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyReportSourceDocument.atomic_statements required"
        )
    if "documentContent" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk_list

        out["document_content"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_annotated_chunk_list.deserialize_json(
                data["documentContent"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyReportSourceDocument.document_content required"
        )
    return out
