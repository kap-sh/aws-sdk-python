"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteTableType``."""

from typing import Literal, TypeAlias, cast

RouteTableType: TypeAlias = Literal[
    "TRANSIT_GATEWAY_ROUTE_TABLE",
    "CORE_NETWORK_SEGMENT",
    "NETWORK_FUNCTION_GROUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTableType) -> str:
    return value


def deserialize_json(data: str) -> RouteTableType:
    return cast(RouteTableType, data)
