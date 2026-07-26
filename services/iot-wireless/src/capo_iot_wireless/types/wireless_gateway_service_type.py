"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayServiceType``."""

from typing import Literal, TypeAlias, cast

WirelessGatewayServiceType: TypeAlias = Literal[
    "CUPS",
    "LNS",
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayServiceType) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayServiceType:
    return cast(WirelessGatewayServiceType, data)
