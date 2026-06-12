"""Generated from Smithy shape ``com.amazonaws.resiliencehub#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

EventType: TypeAlias = Literal[
    "ScheduledAssessmentFailure",
    "DriftDetected",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ScheduledAssessmentFailure",
        "DriftDetected",
    )
)


def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {data!r}")
    return cast(EventType, data)
