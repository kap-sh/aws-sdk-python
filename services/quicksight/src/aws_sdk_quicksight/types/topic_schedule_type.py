"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicScheduleType``."""

from typing import Literal, TypeAlias, cast

TopicScheduleType: TypeAlias = Literal[
    "HOURLY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicScheduleType) -> str:
    return value


def deserialize_json(data: str) -> TopicScheduleType:
    return cast(TopicScheduleType, data)
