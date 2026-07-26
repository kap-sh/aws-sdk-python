"""Generated from Smithy shape ``com.amazonaws.appflow#ScheduleFrequencyType``."""

from typing import Literal, TypeAlias, cast

ScheduleFrequencyType: TypeAlias = Literal[
    "BYMINUTE",
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
    "ONCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleFrequencyType) -> str:
    return value


def deserialize_json(data: str) -> ScheduleFrequencyType:
    return cast(ScheduleFrequencyType, data)
