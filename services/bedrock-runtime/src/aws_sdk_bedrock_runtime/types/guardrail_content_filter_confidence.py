"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentFilterConfidence``."""

from typing import Literal, TypeAlias, cast

GuardrailContentFilterConfidence: TypeAlias = Literal[
    "NONE",
    "LOW",
    "MEDIUM",
    "HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilterConfidence) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentFilterConfidence:
    return cast(GuardrailContentFilterConfidence, data)
