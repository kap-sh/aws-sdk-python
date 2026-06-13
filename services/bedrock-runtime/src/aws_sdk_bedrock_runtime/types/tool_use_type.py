"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolUseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

ToolUseType: TypeAlias = Literal["server_tool_use",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("server_tool_use",))


def serialize_json(value: ToolUseType) -> str:
    return value


def deserialize_json(data: str) -> ToolUseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ToolUseType value: {data!r}")
    return cast(ToolUseType, data)
