"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayTaskStatus``."""

from typing import Literal, TypeAlias, cast

WirelessGatewayTaskStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "FIRST_RETRY",
    "SECOND_RETRY",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WirelessGatewayTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayTaskStatus:
    return cast(WirelessGatewayTaskStatus, data)
