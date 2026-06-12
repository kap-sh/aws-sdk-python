"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayEvent``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>The event for a log message, if the log message is tied to a wireless gateway.</p>"""
WirelessGatewayEvent: TypeAlias = Literal[
    "CUPS_Request",
    "Certificate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUPS_Request",
        "Certificate",
    )
)


def serialize_json(value: WirelessGatewayEvent) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayEvent:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WirelessGatewayEvent value: {data!r}")
    return cast(WirelessGatewayEvent, data)
