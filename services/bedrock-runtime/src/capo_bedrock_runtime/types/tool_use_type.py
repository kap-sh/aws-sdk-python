"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolUseType``."""

from typing import Literal, TypeAlias, cast

ToolUseType: TypeAlias = Literal["server_tool_use",]


# --- restJson1 ser/de ---
def serialize_json(value: ToolUseType) -> str:
    return value


def deserialize_json(data: str) -> ToolUseType:
    return cast(ToolUseType, data)
