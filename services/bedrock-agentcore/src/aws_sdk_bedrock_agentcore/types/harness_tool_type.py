"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolType``."""

from typing import Literal, TypeAlias, cast

HarnessToolType: TypeAlias = Literal[
    "remote_mcp",
    "agentcore_browser",
    "agentcore_gateway",
    "inline_function",
    "agentcore_code_interpreter",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolType) -> str:
    return value


def deserialize_json(data: str) -> HarnessToolType:
    return cast(HarnessToolType, data)
