"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#TriggerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events_data.errors import DeserializationError

TriggerType: TypeAlias = Literal["SNOOZE_TIMEOUT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SNOOZE_TIMEOUT",))


def serialize_json(value: TriggerType) -> str:
    return value


def deserialize_json(data: str) -> TriggerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TriggerType value: {data!r}")
    return cast(TriggerType, data)
