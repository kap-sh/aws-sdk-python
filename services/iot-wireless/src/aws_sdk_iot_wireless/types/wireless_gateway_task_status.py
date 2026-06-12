"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessGatewayTaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

WirelessGatewayTaskStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "FIRST_RETRY",
    "SECOND_RETRY",
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "FIRST_RETRY",
        "SECOND_RETRY",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: WirelessGatewayTaskStatus) -> str:
    return value


def deserialize_json(data: str) -> WirelessGatewayTaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WirelessGatewayTaskStatus value: {data!r}")
    return cast(WirelessGatewayTaskStatus, data)
