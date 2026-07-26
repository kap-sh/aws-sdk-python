"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDeleteKnowledgeBaseRequestKnowledgeBaseIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.knowledge_base_id

BatchDeleteKnowledgeBaseRequestKnowledgeBaseIdsList: TypeAlias = list[
    "capo_quicksight.types.knowledge_base_id.KnowledgeBaseId"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteKnowledgeBaseRequestKnowledgeBaseIdsList) -> list:
    return list(value)


def deserialize_json(data: list) -> BatchDeleteKnowledgeBaseRequestKnowledgeBaseIdsList:
    return list(data)
