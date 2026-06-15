"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessToolType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

HarnessToolType: TypeAlias = Literal[
    "remote_mcp",
    "agentcore_browser",
    "agentcore_gateway",
    "inline_function",
    "agentcore_code_interpreter",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "remote_mcp",
        "agentcore_browser",
        "agentcore_gateway",
        "inline_function",
        "agentcore_code_interpreter",
    )
)


def serialize_json(value: HarnessToolType) -> str:
    return value


def deserialize_json(data: str) -> HarnessToolType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HarnessToolType value: {data!r}")
    return cast(HarnessToolType, data)
