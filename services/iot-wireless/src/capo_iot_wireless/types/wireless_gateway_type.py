"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayType``."""

from typing import Literal, TypeAlias, cast

"""<p>The wireless gateway type.</p>"""
WirelessGatewayType: TypeAlias = Literal["LoRaWAN",]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayType) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayType:
    return cast(WirelessGatewayType, data)
