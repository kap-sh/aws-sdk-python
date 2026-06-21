"""Generated from Smithy shape ``com.amazonaws.bedrockagent#InlineContentType``."""

from typing import Literal, TypeAlias, cast

InlineContentType: TypeAlias = Literal[
    "BYTE",
    "TEXT",
]


# --- restJson1 ser/de ---
def serialize_json(value: InlineContentType) -> str:
    return value


def deserialize_json(data: str) -> InlineContentType:
    return cast(InlineContentType, data)
