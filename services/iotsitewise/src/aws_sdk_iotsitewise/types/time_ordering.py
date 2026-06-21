"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TimeOrdering``."""

from typing import Literal, TypeAlias, cast

TimeOrdering: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeOrdering) -> str:
    return value


def deserialize_json(data: str) -> TimeOrdering:
    return cast(TimeOrdering, data)
