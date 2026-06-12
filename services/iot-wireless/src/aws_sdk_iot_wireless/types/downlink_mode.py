"""Generated from Smithy shape ``com.amazonaws.iotwireless#DownlinkMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

DownlinkMode: TypeAlias = Literal[
    "SEQUENTIAL",
    "CONCURRENT",
    "USING_UPLINK_GATEWAY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEQUENTIAL",
        "CONCURRENT",
        "USING_UPLINK_GATEWAY",
    )
)


def serialize_json(value: DownlinkMode) -> str:
    return value


def deserialize_json(data: str) -> DownlinkMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DownlinkMode value: {data!r}")
    return cast(DownlinkMode, data)
