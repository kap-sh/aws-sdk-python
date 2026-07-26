"""Generated from Smithy shape ``com.amazonaws.workdocs#FolderContentType``."""

from typing import Literal, TypeAlias, cast

FolderContentType: TypeAlias = Literal[
    "ALL",
    "DOCUMENT",
    "FOLDER",
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderContentType) -> str:
    return value


def deserialize_json(data: str) -> FolderContentType:
    return cast(FolderContentType, data)
