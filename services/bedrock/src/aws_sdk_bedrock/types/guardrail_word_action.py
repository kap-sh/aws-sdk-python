"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailWordAction``."""

from typing import Literal, TypeAlias, cast

GuardrailWordAction: TypeAlias = Literal[
    "BLOCK",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailWordAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailWordAction:
    return cast(GuardrailWordAction, data)
