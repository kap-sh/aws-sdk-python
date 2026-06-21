"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoice#EventType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    return cast(EventType, data)
