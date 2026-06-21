"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#KnowledgeBaseQueryType``."""

from typing import Literal, TypeAlias, cast

KnowledgeBaseQueryType: TypeAlias = Literal[
    "TEXT",
    "IMAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseQueryType) -> str:
    return value


def deserialize_json(data: str) -> KnowledgeBaseQueryType:
    return cast(KnowledgeBaseQueryType, data)
