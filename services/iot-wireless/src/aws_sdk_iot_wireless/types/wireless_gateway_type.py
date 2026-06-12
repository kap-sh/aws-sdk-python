"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>The wireless gateway type.</p>"""
WirelessGatewayType: TypeAlias = Literal["LoRaWAN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LoRaWAN",))


def serialize_json(value: WirelessGatewayType) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WirelessGatewayType value: {data!r}")
    return cast(WirelessGatewayType, data)
