"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptRouterType``."""

from typing import Literal, TypeAlias, cast

PromptRouterType: TypeAlias = Literal[
    "custom",
    "default",
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptRouterType) -> str:
    return value


def deserialize_json(data: str) -> PromptRouterType:
    return cast(PromptRouterType, data)
