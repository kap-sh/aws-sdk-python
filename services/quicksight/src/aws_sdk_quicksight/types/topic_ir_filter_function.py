"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRFilterFunction``."""

from typing import Literal, TypeAlias, cast

TopicIRFilterFunction: TypeAlias = Literal[
    "CONTAINS",
    "EXACT",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS_STRING",
    "PREVIOUS",
    "THIS",
    "LAST",
    "NEXT",
    "NOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRFilterFunction) -> str:
    return value


def deserialize_json(data: str) -> TopicIRFilterFunction:
    return cast(TopicIRFilterFunction, data)
