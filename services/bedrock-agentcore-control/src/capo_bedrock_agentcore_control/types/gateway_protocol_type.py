"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayProtocolType``."""

from typing import Literal, TypeAlias, cast

GatewayProtocolType: TypeAlias = Literal["MCP",]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayProtocolType) -> str:
    return value


def deserialize_json(data: str) -> GatewayProtocolType:
    return cast(GatewayProtocolType, data)
