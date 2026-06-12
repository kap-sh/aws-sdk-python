"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayIdType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

WirelessGatewayIdType: TypeAlias = Literal[
    "GatewayEui",
    "WirelessGatewayId",
    "ThingName",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GatewayEui",
        "WirelessGatewayId",
        "ThingName",
    )
)


def serialize_json(value: WirelessGatewayIdType) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayIdType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WirelessGatewayIdType value: {data!r}")
    return cast(WirelessGatewayIdType, data)
