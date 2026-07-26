"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyRunStatus``."""

from typing import Literal, TypeAlias, cast

JourneyRunStatus: TypeAlias = Literal[
    "SCHEDULED",
    "RUNNING",
    "COMPLETED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: JourneyRunStatus) -> str:
    return value


def deserialize_json(data: str) -> JourneyRunStatus:
    return cast(JourneyRunStatus, data)
