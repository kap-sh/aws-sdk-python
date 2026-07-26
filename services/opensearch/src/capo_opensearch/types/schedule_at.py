"""Generated from Smithy shape ``com.amazonaws.opensearch#ScheduleAt``."""

from typing import Literal, TypeAlias, cast

ScheduleAt: TypeAlias = Literal[
    "NOW",
    "TIMESTAMP",
    "OFF_PEAK_WINDOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleAt) -> str:
    return value


def deserialize_json(data: str) -> ScheduleAt:
    return cast(ScheduleAt, data)
