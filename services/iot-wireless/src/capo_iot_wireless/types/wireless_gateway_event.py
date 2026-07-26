"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayEvent``."""

from typing import Literal, TypeAlias, cast

"""<p>The event for a log message, if the log message is tied to a wireless gateway.</p>"""
WirelessGatewayEvent: TypeAlias = Literal[
    "CUPS_Request",
    "Certificate",
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayEvent) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayEvent:
    return cast(WirelessGatewayEvent, data)
