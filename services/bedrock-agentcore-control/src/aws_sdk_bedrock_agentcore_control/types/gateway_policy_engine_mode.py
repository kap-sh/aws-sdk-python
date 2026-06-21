"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayPolicyEngineMode``."""

from typing import Literal, TypeAlias, cast

GatewayPolicyEngineMode: TypeAlias = Literal[
    "LOG_ONLY",
    "ENFORCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayPolicyEngineMode) -> str:
    return value


def deserialize_json(data: str) -> GatewayPolicyEngineMode:
    return cast(GatewayPolicyEngineMode, data)
