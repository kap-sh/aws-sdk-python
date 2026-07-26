"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDeleteKnowledgeBaseSuccess``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.knowledge_base_arn
    import capo_quicksight.types.knowledge_base_id


class BatchDeleteKnowledgeBaseSuccess(TypedDict, closed=True):
    knowledge_base_id: "capo_quicksight.types.knowledge_base_id.KnowledgeBaseId"
    """<p>The unique identifier of the successfully deleted knowledge base.</p>"""
    knowledge_base_arn: "capo_quicksight.types.knowledge_base_arn.KnowledgeBaseArn"
    """<p>The ARN of the successfully deleted knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteKnowledgeBaseSuccess) -> dict:
    out: dict = {}
    out["KnowledgeBaseId"] = value["knowledge_base_id"]
    out["KnowledgeBaseArn"] = value["knowledge_base_arn"]
    return out


def deserialize_json(data: dict) -> BatchDeleteKnowledgeBaseSuccess:
    out: BatchDeleteKnowledgeBaseSuccess = {}  # type: ignore[typeddict-item]
    if "KnowledgeBaseId" in data:
        out["knowledge_base_id"] = data["KnowledgeBaseId"]
    else:
        raise DeserializationError(
            "BatchDeleteKnowledgeBaseSuccess.knowledge_base_id required"
        )
    if "KnowledgeBaseArn" in data:
        out["knowledge_base_arn"] = data["KnowledgeBaseArn"]
    else:
        raise DeserializationError(
            "BatchDeleteKnowledgeBaseSuccess.knowledge_base_arn required"
        )
    return out
