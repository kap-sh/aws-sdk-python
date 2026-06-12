"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

Type: TypeAlias = Literal[
    "CONVERSATION",
    "DICTATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONVERSATION",
        "DICTATION",
    )
)


def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Type value: {data!r}")
    return cast(Type, data)
