"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentFilterStrength``."""

from typing import Literal, TypeAlias, cast

GuardrailContentFilterStrength: TypeAlias = Literal[
    "NONE",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilterStrength) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentFilterStrength:
    return cast(GuardrailContentFilterStrength, data)
