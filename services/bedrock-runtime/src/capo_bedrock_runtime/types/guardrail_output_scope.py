"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOutputScope``."""

from typing import Literal, TypeAlias, cast

GuardrailOutputScope: TypeAlias = Literal[
    "INTERVENTIONS",
    "FULL",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailOutputScope) -> str:
    return value


def deserialize_json(data: str) -> GuardrailOutputScope:
    return cast(GuardrailOutputScope, data)
