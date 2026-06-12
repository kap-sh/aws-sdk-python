"""Generated from Smithy shape ``com.amazonaws.iotwireless#DimensionName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

DimensionName: TypeAlias = Literal[
    "DeviceId",
    "GatewayId",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DeviceId",
        "GatewayId",
    )
)


def serialize_json(value: DimensionName) -> str:
    return value


def deserialize_json(data: str) -> DimensionName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DimensionName value: {data!r}")
    return cast(DimensionName, data)
