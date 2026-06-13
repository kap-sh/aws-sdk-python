"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentFilterStrength``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailContentFilterStrength: TypeAlias = Literal[
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


def serialize_json(value: GuardrailContentFilterStrength) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentFilterStrength:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailContentFilterStrength value: {data!r}"
        )
    return cast(GuardrailContentFilterStrength, data)
