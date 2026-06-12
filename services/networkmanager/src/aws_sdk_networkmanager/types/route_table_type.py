"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteTableType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

RouteTableType: TypeAlias = Literal[
    "TRANSIT_GATEWAY_ROUTE_TABLE",
    "CORE_NETWORK_SEGMENT",
    "NETWORK_FUNCTION_GROUP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRANSIT_GATEWAY_ROUTE_TABLE",
        "CORE_NETWORK_SEGMENT",
        "NETWORK_FUNCTION_GROUP",
    )
)


def serialize_json(value: RouteTableType) -> str:
    return value


def deserialize_json(data: str) -> RouteTableType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTableType value: {data!r}")
    return cast(RouteTableType, data)
