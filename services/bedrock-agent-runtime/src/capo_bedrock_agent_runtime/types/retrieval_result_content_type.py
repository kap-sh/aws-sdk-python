"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultContentType``."""

from typing import Literal, TypeAlias, cast

RetrievalResultContentType: TypeAlias = Literal[
    "TEXT",
    "IMAGE",
    "ROW",
    "AUDIO",
    "VIDEO",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultContentType) -> str:
    return value


def deserialize_json(data: str) -> RetrievalResultContentType:
    return cast(RetrievalResultContentType, data)
