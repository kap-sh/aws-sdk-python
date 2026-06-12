"""Generated from Smithy shape ``com.amazonaws.iotevents#AlarmModelVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events.errors import DeserializationError

AlarmModelVersionStatus: TypeAlias = Literal[
    "ACTIVE",
    "ACTIVATING",
    "INACTIVE",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "ACTIVATING",
        "INACTIVE",
        "FAILED",
    )
)


def serialize_json(value: AlarmModelVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> AlarmModelVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlarmModelVersionStatus value: {data!r}")
    return cast(AlarmModelVersionStatus, data)
