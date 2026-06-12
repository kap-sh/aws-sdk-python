"""Generated from Smithy shape ``com.amazonaws.connect#WeekdayOccurrenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.weekday_occurrence_integer

WeekdayOccurrenceList: TypeAlias = list[
    "aws_sdk_connect.types.weekday_occurrence_integer.WeekdayOccurrenceInteger"
]


# --- restJson1 ser/de ---
def serialize_json(value: WeekdayOccurrenceList) -> list:
    return list(value)


def deserialize_json(data: list) -> WeekdayOccurrenceList:
    return list(data)
