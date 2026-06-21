"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicTimeGranularity``."""

from typing import Literal, TypeAlias, cast

TopicTimeGranularity: TypeAlias = Literal[
    "SECOND",
    "MINUTE",
    "HOUR",
    "DAY",
    "WEEK",
    "MONTH",
    "QUARTER",
    "YEAR",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicTimeGranularity) -> str:
    return value


def deserialize_json(data: str) -> TopicTimeGranularity:
    return cast(TopicTimeGranularity, data)
