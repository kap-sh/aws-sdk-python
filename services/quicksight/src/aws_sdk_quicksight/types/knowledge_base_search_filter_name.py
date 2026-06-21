"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSearchFilterName``."""

from typing import Literal, TypeAlias, cast

KnowledgeBaseSearchFilterName: TypeAlias = Literal[
    "KNOWLEDGE_BASE_ID",
    "KNOWLEDGE_BASE_NAME",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "KNOWLEDGE_BASE_SIZE_BYTES",
    "PRIMARY_OWNER",
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSearchFilterName) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseSearchFilterName:
    return cast(KnowledgeBaseSearchFilterName, data)
