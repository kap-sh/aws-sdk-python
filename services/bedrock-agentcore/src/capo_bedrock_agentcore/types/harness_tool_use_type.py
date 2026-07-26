"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolUseType``."""

from typing import Literal, TypeAlias, cast

HarnessToolUseType: TypeAlias = Literal[
    "tool_use",
    "server_tool_use",
    "mcp_tool_use",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolUseType) -> str:
    return value


def deserialize_json(data: str) -> HarnessToolUseType:
    return cast(HarnessToolUseType, data)
