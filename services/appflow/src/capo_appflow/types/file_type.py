"""Generated from Smithy shape ``com.amazonaws.appflow#FileType``."""

from typing import Literal, TypeAlias, cast

FileType: TypeAlias = Literal[
    "CSV",
    "JSON",
    "PARQUET",
]


# --- restJson1 ser/de ---
def serialize_json(value: FileType) -> str:
    return value


def deserialize_json(data: str) -> FileType:
    return cast(FileType, data)
