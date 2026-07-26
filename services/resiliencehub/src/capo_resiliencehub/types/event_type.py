"""Generated from Smithy shape ``com.amazonaws.resiliencehub#EventType``."""

from typing import Literal, TypeAlias, cast

EventType: TypeAlias = Literal[
    "ScheduledAssessmentFailure",
    "DriftDetected",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    return cast(EventType, data)
