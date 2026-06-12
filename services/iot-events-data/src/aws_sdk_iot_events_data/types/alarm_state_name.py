"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#AlarmStateName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events_data.errors import DeserializationError

AlarmStateName: TypeAlias = Literal[
    "DISABLED",
    "NORMAL",
    "ACTIVE",
    "ACKNOWLEDGED",
    "SNOOZE_DISABLED",
    "LATCHED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "NORMAL",
        "ACTIVE",
        "ACKNOWLEDGED",
        "SNOOZE_DISABLED",
        "LATCHED",
    )
)


def serialize_json(value: AlarmStateName) -> str:
    return value


def deserialize_json(data: str) -> AlarmStateName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlarmStateName value: {data!r}")
    return cast(AlarmStateName, data)
