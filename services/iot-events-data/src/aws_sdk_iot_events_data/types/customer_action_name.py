"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#CustomerActionName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events_data.errors import DeserializationError

CustomerActionName: TypeAlias = Literal[
    "SNOOZE",
    "ENABLE",
    "DISABLE",
    "ACKNOWLEDGE",
    "RESET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SNOOZE",
        "ENABLE",
        "DISABLE",
        "ACKNOWLEDGE",
        "RESET",
    )
)


def serialize_json(value: CustomerActionName) -> str:
    return value


def deserialize_json(data: str) -> CustomerActionName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomerActionName value: {data!r}")
    return cast(CustomerActionName, data)
