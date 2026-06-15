"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolUseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

HarnessToolUseType: TypeAlias = Literal[
    "tool_use",
    "server_tool_use",
    "mcp_tool_use",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "tool_use",
        "server_tool_use",
        "mcp_tool_use",
    )
)


def serialize_json(value: HarnessToolUseType) -> str:
    return value


def deserialize_json(data: str) -> HarnessToolUseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HarnessToolUseType value: {data!r}")
    return cast(HarnessToolUseType, data)
