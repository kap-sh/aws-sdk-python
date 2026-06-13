"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRFilterFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: TopicIRFilterFunction) -> str:
    return value


def deserialize_json(data: str) -> TopicIRFilterFunction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopicIRFilterFunction value: {data!r}")
    return cast(TopicIRFilterFunction, data)
