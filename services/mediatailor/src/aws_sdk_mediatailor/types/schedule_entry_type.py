"""Generated from Smithy shape ``com.amazonaws.mediatailor#ScheduleEntryType``."""

from typing import Literal, TypeAlias, cast

ScheduleEntryType: TypeAlias = Literal[
    "PROGRAM",
    "FILLER_SLATE",
    "ALTERNATE_MEDIA",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScheduleEntryType) -> str:
    return value


def deserialize_json(data: str) -> ScheduleEntryType:
    return cast(ScheduleEntryType, data)
