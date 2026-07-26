"""Generated from Smithy shape ``com.amazonaws.deadline#FileSystemLocationType``."""

from typing import Literal, TypeAlias, cast

FileSystemLocationType: TypeAlias = Literal[
    "SHARED",
    "LOCAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemLocationType) -> str:
    return value


def deserialize_json(data: str) -> FileSystemLocationType:
    return cast(FileSystemLocationType, data)
