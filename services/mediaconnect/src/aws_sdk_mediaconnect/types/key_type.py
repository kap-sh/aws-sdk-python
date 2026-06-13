"""Generated from Smithy shape ``com.amazonaws.mediaconnect#KeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

KeyType: TypeAlias = Literal[
    "speke",
    "static-key",
    "srt-password",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "speke",
        "static-key",
        "srt-password",
    )
)


def serialize_json(value: KeyType) -> str:
    return value


def deserialize_json(data: str) -> KeyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyType value: {data!r}")
    return cast(KeyType, data)
