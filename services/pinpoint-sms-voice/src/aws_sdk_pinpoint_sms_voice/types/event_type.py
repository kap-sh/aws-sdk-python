"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint_sms_voice.errors import DeserializationError

"""The types of events that are sent to the event destination."""
EventType: TypeAlias = Literal[
    "INITIATED_CALL",
    "RINGING",
    "ANSWERED",
    "COMPLETED_CALL",
    "BUSY",
    "FAILED",
    "NO_ANSWER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIATED_CALL",
        "RINGING",
        "ANSWERED",
        "COMPLETED_CALL",
        "BUSY",
        "FAILED",
        "NO_ANSWER",
    )
)


def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {data!r}")
    return cast(EventType, data)
