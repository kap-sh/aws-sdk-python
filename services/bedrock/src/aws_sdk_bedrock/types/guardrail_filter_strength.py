"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailFilterStrength``."""

from typing import Literal, TypeAlias, cast

GuardrailFilterStrength: TypeAlias = Literal[
    "NONE",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailFilterStrength) -> str:
    return value


def deserialize_json(data: str) -> GuardrailFilterStrength:
    return cast(GuardrailFilterStrength, data)
