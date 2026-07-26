"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ItemType``."""

from typing import Literal, TypeAlias, cast

ItemType: TypeAlias = Literal[
    "pronunciation",
    "punctuation",
]


# --- restJson1 ser/de ---
def serialize_json(value: ItemType) -> str:
    return value


def deserialize_json(data: str) -> ItemType:
    return cast(ItemType, data)
