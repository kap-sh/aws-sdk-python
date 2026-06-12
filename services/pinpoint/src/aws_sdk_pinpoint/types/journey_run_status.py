"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

JourneyRunStatus: TypeAlias = Literal[
    "SCHEDULED",
    "RUNNING",
    "COMPLETED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "RUNNING",
        "COMPLETED",
        "CANCELLED",
    )
)


def serialize_json(value: JourneyRunStatus) -> str:
    return value


def deserialize_json(data: str) -> JourneyRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JourneyRunStatus value: {data!r}")
    return cast(JourneyRunStatus, data)
