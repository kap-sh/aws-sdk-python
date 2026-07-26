"""Generated from Smithy shape ``com.amazonaws.ebs#SSEType``."""

from typing import Literal, TypeAlias, cast

SSEType: TypeAlias = Literal[
    "sse-ebs",
    "sse-kms",
    "none",
]


# --- restJson1 ser/de ---
def serialize_json(value: SSEType) -> str:
    return value


def deserialize_json(data: str) -> SSEType:
    return cast(SSEType, data)
