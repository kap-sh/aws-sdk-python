"""Generated from Smithy shape ``com.amazonaws.deadline#FileSystemLocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

FileSystemLocationType: TypeAlias = Literal[
    "SHARED",
    "LOCAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHARED",
        "LOCAL",
    )
)


def serialize_json(value: FileSystemLocationType) -> str:
    return value


def deserialize_json(data: str) -> FileSystemLocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileSystemLocationType value: {data!r}")
    return cast(FileSystemLocationType, data)
