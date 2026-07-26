"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayRuleStatus``."""

from typing import Literal, TypeAlias, cast

GatewayRuleStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayRuleStatus) -> str:
    return value


def deserialize_json(data: str) -> GatewayRuleStatus:
    return cast(GatewayRuleStatus, data)
