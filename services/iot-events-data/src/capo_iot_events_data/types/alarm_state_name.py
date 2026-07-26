"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#AlarmStateName``."""

from typing import Literal, TypeAlias, cast

AlarmStateName: TypeAlias = Literal[
    "DISABLED",
    "NORMAL",
    "ACTIVE",
    "ACKNOWLEDGED",
    "SNOOZE_DISABLED",
    "LATCHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AlarmStateName) -> str:
    return value


def deserialize_json(data: str) -> AlarmStateName:
    return cast(AlarmStateName, data)
