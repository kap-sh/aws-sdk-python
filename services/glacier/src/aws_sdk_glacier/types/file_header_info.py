"""Generated from Smithy shape ``com.amazonaws.glacier#FileHeaderInfo``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glacier.errors import DeserializationError

FileHeaderInfo: TypeAlias = Literal[
    "USE",
    "IGNORE",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USE",
        "IGNORE",
        "NONE",
    )
)


def serialize_json(value: FileHeaderInfo) -> str:
    return value


def deserialize_json(data: str) -> FileHeaderInfo:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileHeaderInfo value: {data!r}")
    return cast(FileHeaderInfo, data)
