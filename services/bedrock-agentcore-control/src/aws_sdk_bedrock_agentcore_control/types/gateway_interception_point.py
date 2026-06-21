"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayInterceptionPoint``."""

from typing import Literal, TypeAlias, cast

GatewayInterceptionPoint: TypeAlias = Literal[
    "REQUEST",
    "RESPONSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayInterceptionPoint) -> str:
    return value


def deserialize_json(data: str) -> GatewayInterceptionPoint:
    return cast(GatewayInterceptionPoint, data)
