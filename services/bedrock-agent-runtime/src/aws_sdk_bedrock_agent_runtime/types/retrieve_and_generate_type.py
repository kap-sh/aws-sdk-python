"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrieveAndGenerateType``."""

from typing import Literal, TypeAlias, cast

RetrieveAndGenerateType: TypeAlias = Literal[
    "KNOWLEDGE_BASE",
    "EXTERNAL_SOURCES",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveAndGenerateType) -> str:
    return value


def deserialize_json(data: str) -> RetrieveAndGenerateType:
    return cast(RetrieveAndGenerateType, data)
