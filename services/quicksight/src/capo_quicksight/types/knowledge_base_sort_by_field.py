"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSortByField``."""

from typing import Literal, TypeAlias, cast

KnowledgeBaseSortByField: TypeAlias = Literal[
    "KNOWLEDGE_BASE_SIZE_BYTES",
    "CREATED_AT",
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSortByField) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseSortByField:
    return cast(KnowledgeBaseSortByField, data)
