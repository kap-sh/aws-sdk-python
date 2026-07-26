"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentFilterType``."""

from typing import Literal, TypeAlias, cast

GuardrailContentFilterType: TypeAlias = Literal[
    "SEXUAL",
    "VIOLENCE",
    "HATE",
    "INSULTS",
    "MISCONDUCT",
    "PROMPT_ATTACK",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilterType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentFilterType:
    return cast(GuardrailContentFilterType, data)
