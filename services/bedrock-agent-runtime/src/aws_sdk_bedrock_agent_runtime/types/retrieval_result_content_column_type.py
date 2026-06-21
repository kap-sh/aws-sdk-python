"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultContentColumnType``."""

from typing import Literal, TypeAlias, cast

RetrievalResultContentColumnType: TypeAlias = Literal[
    "BLOB",
    "BOOLEAN",
    "DOUBLE",
    "NULL",
    "LONG",
    "STRING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultContentColumnType) -> str:
    return value


def deserialize_json(data: str) -> RetrievalResultContentColumnType:
    return cast(RetrievalResultContentColumnType, data)
