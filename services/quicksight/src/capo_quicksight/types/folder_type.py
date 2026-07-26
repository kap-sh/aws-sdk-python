"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderType``."""

from typing import Literal, TypeAlias, cast

FolderType: TypeAlias = Literal[
    "SHARED",
    "RESTRICTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderType) -> str:
    return value


def deserialize_json(data: str) -> FolderType:
    return cast(FolderType, data)
