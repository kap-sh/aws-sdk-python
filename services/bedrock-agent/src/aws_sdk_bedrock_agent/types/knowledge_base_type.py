"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBaseType``."""

from typing import Literal, TypeAlias, cast

KnowledgeBaseType: TypeAlias = Literal[
    "VECTOR",
    "KENDRA",
    "SQL",
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseType) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseType:
    return cast(KnowledgeBaseType, data)
