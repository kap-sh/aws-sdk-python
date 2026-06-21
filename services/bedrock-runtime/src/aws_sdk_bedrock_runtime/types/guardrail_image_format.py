"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailImageFormat``."""

from typing import Literal, TypeAlias, cast

GuardrailImageFormat: TypeAlias = Literal[
    "png",
    "jpeg",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailImageFormat) -> str:
    return value


def deserialize_json(data: str) -> GuardrailImageFormat:
    return cast(GuardrailImageFormat, data)
