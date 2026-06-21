"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptTemplateType``."""

from typing import Literal, TypeAlias, cast

PromptTemplateType: TypeAlias = Literal[
    "TEXT",
    "CHAT",
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptTemplateType) -> str:
    return value


def deserialize_json(data: str) -> PromptTemplateType:
    return cast(PromptTemplateType, data)
