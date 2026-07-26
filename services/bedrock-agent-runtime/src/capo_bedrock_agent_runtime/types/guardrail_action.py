"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailAction``."""

from typing import Literal, TypeAlias, cast

GuardrailAction: TypeAlias = Literal[
    "INTERVENED",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailAction:
    return cast(GuardrailAction, data)
