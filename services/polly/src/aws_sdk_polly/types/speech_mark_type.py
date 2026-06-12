"""Generated from Smithy shape ``com.amazonaws.polly#SpeechMarkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_polly.errors import DeserializationError

SpeechMarkType: TypeAlias = Literal[
    "sentence",
    "ssml",
    "viseme",
    "word",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "sentence",
        "ssml",
        "viseme",
        "word",
    )
)


def serialize_json(value: SpeechMarkType) -> str:
    return value


def deserialize_json(data: str) -> SpeechMarkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SpeechMarkType value: {data!r}")
    return cast(SpeechMarkType, data)
