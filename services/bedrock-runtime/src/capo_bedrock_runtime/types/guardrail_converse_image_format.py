"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseImageFormat``."""

from typing import Literal, TypeAlias, cast

GuardrailConverseImageFormat: TypeAlias = Literal[
    "png",
    "jpeg",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConverseImageFormat) -> str:
    return value


def deserialize_json(data: str) -> GuardrailConverseImageFormat:
    return cast(GuardrailConverseImageFormat, data)
