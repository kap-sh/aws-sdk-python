"""Generated from Smithy shape ``com.amazonaws.connect#FileStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

FileStatusType: TypeAlias = Literal[
    "APPROVED",
    "REJECTED",
    "PROCESSING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVED",
        "REJECTED",
        "PROCESSING",
        "FAILED",
    )
)


def serialize_json(value: FileStatusType) -> str:
    return value


def deserialize_json(data: str) -> FileStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileStatusType value: {data!r}")
    return cast(FileStatusType, data)
