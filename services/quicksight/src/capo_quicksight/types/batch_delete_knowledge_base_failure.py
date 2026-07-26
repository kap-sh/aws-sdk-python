"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDeleteKnowledgeBaseFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.knowledge_base_id


class BatchDeleteKnowledgeBaseFailure(TypedDict, closed=True):
    knowledge_base_id: "capo_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier of the knowledge base that failed to be deleted.</p>"""
    error_code: "str"
    """<p>The error code for the deletion failure.</p>"""
    error_message: "str"
    """<p>The error message for the deletion failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteKnowledgeBaseFailure) -> dict:
    out: dict = {}
    out["KnowledgeBaseId"] = value["knowledge_base_id"]
    out["ErrorCode"] = value["error_code"]
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchDeleteKnowledgeBaseFailure:
    out: BatchDeleteKnowledgeBaseFailure = {}  # type: ignore[typeddict-item]
    if "KnowledgeBaseId" in data:
        out["knowledge_base_id"] = data["KnowledgeBaseId"]
    else:
        raise DeserializationError(
            "BatchDeleteKnowledgeBaseFailure.knowledge_base_id required"
        )
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError(
            "BatchDeleteKnowledgeBaseFailure.error_code required"
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    else:
        raise DeserializationError(
            "BatchDeleteKnowledgeBaseFailure.error_message required"
        )
    return out
