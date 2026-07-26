"""Generated from Smithy shape ``com.amazonaws.iotwireless#IdentifierType``."""

from typing import Literal, TypeAlias, cast

IdentifierType: TypeAlias = Literal[
    "PartnerAccountId",
    "DevEui",
    "GatewayEui",
    "WirelessDeviceId",
    "WirelessGatewayId",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentifierType) -> str:
    return value


def deserialize_json(data: str) -> IdentifierType:
    return cast(IdentifierType, data)
