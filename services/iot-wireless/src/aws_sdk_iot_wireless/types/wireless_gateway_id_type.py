"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayIdType``."""

from typing import Literal, TypeAlias, cast

WirelessGatewayIdType: TypeAlias = Literal[
    "GatewayEui",
    "WirelessGatewayId",
    "ThingName",
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayIdType) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayIdType:
    return cast(WirelessGatewayIdType, data)
