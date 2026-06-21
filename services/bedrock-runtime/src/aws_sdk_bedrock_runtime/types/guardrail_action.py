"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAction``."""

from typing import Literal, TypeAlias, cast

GuardrailAction: TypeAlias = Literal[
    "NONE",
    "GUARDRAIL_INTERVENED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailAction:
    return cast(GuardrailAction, data)
