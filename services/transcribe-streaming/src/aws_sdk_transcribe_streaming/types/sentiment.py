"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#Sentiment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

Sentiment: TypeAlias = Literal[
    "POSITIVE",
    "NEGATIVE",
    "MIXED",
    "NEUTRAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "POSITIVE",
        "NEGATIVE",
        "MIXED",
        "NEUTRAL",
    )
)


def serialize_json(value: Sentiment) -> str:
    return value


def deserialize_json(data: str) -> Sentiment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Sentiment value: {data!r}")
    return cast(Sentiment, data)
