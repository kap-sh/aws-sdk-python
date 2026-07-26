"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicSortDirection``."""

from typing import Literal, TypeAlias, cast

TopicSortDirection: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicSortDirection) -> str:
    return value


def deserialize_json(data: str) -> TopicSortDirection:
    return cast(TopicSortDirection, data)
