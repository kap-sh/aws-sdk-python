"""Generated from Smithy shape ``com.amazonaws.networkmanager#RoutingPolicyDirection``."""

from typing import Literal, TypeAlias, cast

RoutingPolicyDirection: TypeAlias = Literal[
    "inbound",
    "outbound",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingPolicyDirection) -> str:
    return value


def deserialize_json(data: str) -> RoutingPolicyDirection:
    return cast(RoutingPolicyDirection, data)
