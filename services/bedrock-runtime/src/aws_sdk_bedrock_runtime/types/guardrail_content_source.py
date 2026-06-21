"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentSource``."""

from typing import Literal, TypeAlias, cast

GuardrailContentSource: TypeAlias = Literal[
    "INPUT",
    "OUTPUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentSource) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentSource:
    return cast(GuardrailContentSource, data)
