"""Generated from Smithy shape ``com.amazonaws.iotwireless#IdentifierType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

IdentifierType: TypeAlias = Literal[
    "PartnerAccountId",
    "DevEui",
    "GatewayEui",
    "WirelessDeviceId",
    "WirelessGatewayId",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PartnerAccountId",
        "DevEui",
        "GatewayEui",
        "WirelessDeviceId",
        "WirelessGatewayId",
    )
)


def serialize_json(value: IdentifierType) -> str:
    return value


def deserialize_json(data: str) -> IdentifierType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentifierType value: {data!r}")
    return cast(IdentifierType, data)
