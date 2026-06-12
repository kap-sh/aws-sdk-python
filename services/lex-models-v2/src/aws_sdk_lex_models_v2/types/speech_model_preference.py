"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SpeechModelPreference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

SpeechModelPreference: TypeAlias = Literal[
    "Standard",
    "Neural",
    "Deepgram",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Standard",
        "Neural",
        "Deepgram",
    )
)


def serialize_json(value: SpeechModelPreference) -> str:
    return value


def deserialize_json(data: str) -> SpeechModelPreference:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SpeechModelPreference value: {data!r}")
    return cast(SpeechModelPreference, data)
