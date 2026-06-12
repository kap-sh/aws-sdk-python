"""Generated from Smithy shape ``com.amazonaws.iotwireless#BatteryLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>Sidewalk device battery level.</p>"""
BatteryLevel: TypeAlias = Literal[
    "normal",
    "low",
    "critical",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "normal",
        "low",
        "critical",
    )
)


def serialize_json(value: BatteryLevel) -> str:
    return value


def deserialize_json(data: str) -> BatteryLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BatteryLevel value: {data!r}")
    return cast(BatteryLevel, data)
