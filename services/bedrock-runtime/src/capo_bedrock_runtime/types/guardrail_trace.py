"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailTrace``."""

from typing import Literal, TypeAlias, cast

GuardrailTrace: TypeAlias = Literal[
    "enabled",
    "disabled",
    "enabled_full",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTrace) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTrace:
    return cast(GuardrailTrace, data)
