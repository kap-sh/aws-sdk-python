"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayTaskDefinitionType``."""

from typing import Literal, TypeAlias, cast

WirelessGatewayTaskDefinitionType: TypeAlias = Literal["UPDATE",]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayTaskDefinitionType) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayTaskDefinitionType:
    return cast(WirelessGatewayTaskDefinitionType, data)
