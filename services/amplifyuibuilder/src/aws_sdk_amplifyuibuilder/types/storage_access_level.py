"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#StorageAccessLevel``."""

from typing import Literal, TypeAlias, cast

StorageAccessLevel: TypeAlias = Literal[
    "public",
    "protected",
    "private",
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageAccessLevel) -> str:
    return value


def deserialize_json(data: str) -> StorageAccessLevel:
    return cast(StorageAccessLevel, data)
