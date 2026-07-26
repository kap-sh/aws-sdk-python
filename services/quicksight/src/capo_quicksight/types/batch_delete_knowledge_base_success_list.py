"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDeleteKnowledgeBaseSuccessList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.batch_delete_knowledge_base_success

BatchDeleteKnowledgeBaseSuccessList: TypeAlias = list[
    "capo_quicksight.types.batch_delete_knowledge_base_success.BatchDeleteKnowledgeBaseSuccess"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteKnowledgeBaseSuccessList) -> list:
    import capo_quicksight.types.batch_delete_knowledge_base_success

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.batch_delete_knowledge_base_success.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteKnowledgeBaseSuccessList:
    import capo_quicksight.types.batch_delete_knowledge_base_success

    out: BatchDeleteKnowledgeBaseSuccessList = []
    for item in data:
        out.append(
            capo_quicksight.types.batch_delete_knowledge_base_success.deserialize_json(
                item
            )
        )
    return out
