"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayServiceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

WirelessGatewayServiceType: TypeAlias = Literal[
    "CUPS",
    "LNS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUPS",
        "LNS",
    )
)


def serialize_json(value: WirelessGatewayServiceType) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayServiceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WirelessGatewayServiceType value: {data!r}"
        )
    return cast(WirelessGatewayServiceType, data)
