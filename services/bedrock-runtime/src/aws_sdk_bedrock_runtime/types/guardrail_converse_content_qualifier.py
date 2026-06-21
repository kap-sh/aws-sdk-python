"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseContentQualifier``."""

from typing import Literal, TypeAlias, cast

GuardrailConverseContentQualifier: TypeAlias = Literal[
    "grounding_source",
    "query",
    "guard_content",
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConverseContentQualifier) -> str:
    return value


def deserialize_json(data: str) -> GuardrailConverseContentQualifier:
    return cast(GuardrailConverseContentQualifier, data)
