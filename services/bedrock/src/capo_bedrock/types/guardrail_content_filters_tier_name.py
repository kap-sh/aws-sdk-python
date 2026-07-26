"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentFiltersTierName``."""

from typing import Literal, TypeAlias, cast

GuardrailContentFiltersTierName: TypeAlias = Literal[
    "CLASSIC",
    "STANDARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFiltersTierName) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentFiltersTierName:
    return cast(GuardrailContentFiltersTierName, data)
