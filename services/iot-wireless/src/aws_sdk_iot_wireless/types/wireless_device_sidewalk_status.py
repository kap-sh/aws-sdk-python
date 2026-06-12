"""Generated from Smithy shape ``com.amazonaws.iotwireless#WirelessDeviceSidewalkStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

WirelessDeviceSidewalkStatus: TypeAlias = Literal[
    "PROVISIONED",
    "REGISTERED",
    "ACTIVATED",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONED",
        "REGISTERED",
        "ACTIVATED",
        "UNKNOWN",
    )
)


def serialize_json(value: WirelessDeviceSidewalkStatus) -> str:
    return value


def deserialize_json(data: str) -> WirelessDeviceSidewalkStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WirelessDeviceSidewalkStatus value: {data!r}"
        )
    return cast(WirelessDeviceSidewalkStatus, data)
