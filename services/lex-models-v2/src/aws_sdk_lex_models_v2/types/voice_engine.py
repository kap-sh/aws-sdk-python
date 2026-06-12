"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#VoiceEngine``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

VoiceEngine: TypeAlias = Literal[
    "standard",
    "neural",
    "long-form",
    "generative",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "neural",
        "long-form",
        "generative",
    )
)


def serialize_json(value: VoiceEngine) -> str:
    return value


def deserialize_json(data: str) -> VoiceEngine:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VoiceEngine value: {data!r}")
    return cast(VoiceEngine, data)
