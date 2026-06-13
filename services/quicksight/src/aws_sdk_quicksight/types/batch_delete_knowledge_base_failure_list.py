"""Generated from Smithy shape ``com.amazonaws.quicksight#BatchDeleteKnowledgeBaseFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.batch_delete_knowledge_base_failure

BatchDeleteKnowledgeBaseFailureList: TypeAlias = list[
    "aws_sdk_quicksight.types.batch_delete_knowledge_base_failure.BatchDeleteKnowledgeBaseFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteKnowledgeBaseFailureList) -> list:
    import aws_sdk_quicksight.types.batch_delete_knowledge_base_failure

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.batch_delete_knowledge_base_failure.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteKnowledgeBaseFailureList:
    import aws_sdk_quicksight.types.batch_delete_knowledge_base_failure

    out: BatchDeleteKnowledgeBaseFailureList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.batch_delete_knowledge_base_failure.deserialize_json(
                item
            )
        )
    return out
