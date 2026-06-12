"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyStatementReference``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_document_id
    import aws_sdk_bedrock.types.automated_reasoning_policy_statement_id


class AutomatedReasoningPolicyStatementReference(TypedDict):
    document_id: "aws_sdk_bedrock.types.automated_reasoning_policy_document_id.AutomatedReasoningPolicyDocumentId"
    """<p>The unique identifier of the document containing the referenced statement.</p>"""
    statement_id: "aws_sdk_bedrock.types.automated_reasoning_policy_statement_id.AutomatedReasoningPolicyStatementId"
    """<p>The unique identifier of the specific atomic statement being referenced.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyStatementReference) -> dict:
    out: dict = {}
    out["documentId"] = value["document_id"]
    out["statementId"] = value["statement_id"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyStatementReference:
    out: AutomatedReasoningPolicyStatementReference = {}  # type: ignore[typeddict-item]
    if "documentId" in data:
        out["document_id"] = data["documentId"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyStatementReference.document_id required"
        )
    if "statementId" in data:
        out["statement_id"] = data["statementId"]
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyStatementReference.statement_id required"
        )
    return out
