"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FolderType: TypeAlias = Literal[
    "SHARED",
    "RESTRICTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHARED",
        "RESTRICTED",
    )
)


def serialize_json(value: FolderType) -> str:
    return value


def deserialize_json(data: str) -> FolderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FolderType value: {data!r}")
    return cast(FolderType, data)
