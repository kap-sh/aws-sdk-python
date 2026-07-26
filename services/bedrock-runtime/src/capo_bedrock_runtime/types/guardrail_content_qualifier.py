"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentQualifier``."""

from typing import Literal, TypeAlias, cast

GuardrailContentQualifier: TypeAlias = Literal[
    "grounding_source",
    "query",
    "guard_content",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentQualifier) -> str:
    return value


def deserialize_json(data: str) -> GuardrailContentQualifier:
    return cast(GuardrailContentQualifier, data)
