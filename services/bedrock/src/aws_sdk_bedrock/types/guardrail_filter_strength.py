"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailFilterStrength``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailFilterStrength: TypeAlias = Literal[
    "NONE",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "LOW",
        "MEDIUM",
        "HIGH",
    )
)


def serialize_json(value: GuardrailFilterStrength) -> str:
    return value


def deserialize_json(data: str) -> GuardrailFilterStrength:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailFilterStrength value: {data!r}")
    return cast(GuardrailFilterStrength, data)
