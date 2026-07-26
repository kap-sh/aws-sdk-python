"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOwnership``."""

from typing import Literal, TypeAlias, cast

GuardrailOwnership: TypeAlias = Literal[
    "SELF",
    "CROSS_ACCOUNT",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailOwnership) -> str:
    return value


def deserialize_json(data: str) -> GuardrailOwnership:
    return cast(GuardrailOwnership, data)
