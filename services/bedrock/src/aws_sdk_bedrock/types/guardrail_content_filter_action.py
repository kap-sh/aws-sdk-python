"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentFilterAction``."""

from typing import Literal, TypeAlias, cast

GuardrailContentFilterAction: TypeAlias = Literal[
    "BLOCK",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilterAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentFilterAction:
    return cast(GuardrailContentFilterAction, data)
