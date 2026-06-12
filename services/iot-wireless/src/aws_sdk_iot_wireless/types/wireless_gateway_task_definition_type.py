"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayTaskDefinitionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

WirelessGatewayTaskDefinitionType: TypeAlias = Literal["UPDATE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("UPDATE",))


def serialize_json(value: WirelessGatewayTaskDefinitionType) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayTaskDefinitionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WirelessGatewayTaskDefinitionType value: {data!r}"
        )
    return cast(WirelessGatewayTaskDefinitionType, data)
