"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeviceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>Device state defines the device status of sidewalk device.</p>"""
DeviceState: TypeAlias = Literal[
    "Provisioned",
    "RegisteredNotSeen",
    "RegisteredReachable",
    "RegisteredUnreachable",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Provisioned",
        "RegisteredNotSeen",
        "RegisteredReachable",
        "RegisteredUnreachable",
    )
)


def serialize_json(value: DeviceState) -> str:
    return value


def deserialize_json(data: str) -> DeviceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceState value: {data!r}")
    return cast(DeviceState, data)
