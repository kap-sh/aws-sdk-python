"""Generated from Smithy shape ``com.amazonaws.workdocs#FolderContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

FolderContentType: TypeAlias = Literal[
    "ALL",
    "DOCUMENT",
    "FOLDER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "DOCUMENT",
        "FOLDER",
    )
)


def serialize_json(value: FolderContentType) -> str:
    return value


def deserialize_json(data: str) -> FolderContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FolderContentType value: {data!r}")
    return cast(FolderContentType, data)
