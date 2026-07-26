"""Generated from Smithy shape ``com.amazonaws.glacier#FileHeaderInfo``."""

from typing import Literal, TypeAlias, cast

FileHeaderInfo: TypeAlias = Literal[
    "USE",
    "IGNORE",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FileHeaderInfo) -> str:
    return value


def deserialize_json(data: str) -> FileHeaderInfo:
    return cast(FileHeaderInfo, data)
