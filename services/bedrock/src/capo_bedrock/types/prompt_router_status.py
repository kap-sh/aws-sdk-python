"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptRouterStatus``."""

from typing import Literal, TypeAlias, cast

PromptRouterStatus: TypeAlias = Literal["AVAILABLE",]


# --- restJson1 ser/de ---
def serialize_json(value: PromptRouterStatus) -> str:
    return value


def deserialize_json(data: str) -> PromptRouterStatus:
    return cast(PromptRouterStatus, data)
