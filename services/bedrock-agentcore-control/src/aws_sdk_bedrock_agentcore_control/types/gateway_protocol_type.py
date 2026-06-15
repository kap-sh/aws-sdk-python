"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayProtocolType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

GatewayProtocolType: TypeAlias = Literal["MCP",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MCP",))


def serialize_json(value: GatewayProtocolType) -> str:
    return value


def deserialize_json(data: str) -> GatewayProtocolType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GatewayProtocolType value: {data!r}")
    return cast(GatewayProtocolType, data)
