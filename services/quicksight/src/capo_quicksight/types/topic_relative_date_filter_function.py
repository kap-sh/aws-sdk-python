"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicRelativeDateFilterFunction``."""

from typing import Literal, TypeAlias, cast

TopicRelativeDateFilterFunction: TypeAlias = Literal[
    "PREVIOUS",
    "THIS",
    "LAST",
    "NEXT",
    "NOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicRelativeDateFilterFunction) -> str:
    return value


def deserialize_json(data: str) -> TopicRelativeDateFilterFunction:
    return cast(TopicRelativeDateFilterFunction, data)
