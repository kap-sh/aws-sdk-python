"""Generated from Smithy shape ``com.amazonaws.mediastoredata#ItemType``."""

from typing import Literal, TypeAlias, cast

ItemType: TypeAlias = Literal[
    "OBJECT",
    "FOLDER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ItemType) -> str:
    return value


def deserialize_json(data: str) -> ItemType:
    return cast(ItemType, data)
