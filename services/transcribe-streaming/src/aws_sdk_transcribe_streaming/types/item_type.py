"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ItemType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

ItemType: TypeAlias = Literal[
    "pronunciation",
    "punctuation",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "pronunciation",
        "punctuation",
    )
)


def serialize_json(value: ItemType) -> str:
    return value


def deserialize_json(data: str) -> ItemType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ItemType value: {data!r}")
    return cast(ItemType, data)
