"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailStreamProcessingMode``."""

from typing import Literal, TypeAlias, cast

GuardrailStreamProcessingMode: TypeAlias = Literal[
    "sync",
    "async",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailStreamProcessingMode) -> str:
    return value


def deserialize_json(data: str) -> GuardrailStreamProcessingMode:
    return cast(GuardrailStreamProcessingMode, data)
