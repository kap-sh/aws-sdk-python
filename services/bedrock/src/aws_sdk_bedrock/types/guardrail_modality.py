"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailModality``."""

from typing import Literal, TypeAlias, cast

GuardrailModality: TypeAlias = Literal[
    "TEXT",
    "IMAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailModality) -> str:
    return value


def deserialize_json(data: str) -> GuardrailModality:
    return cast(GuardrailModality, data)
