"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicRelativeDateFilterFunction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TopicRelativeDateFilterFunction: TypeAlias = Literal[
    "PREVIOUS",
    "THIS",
    "LAST",
    "NEXT",
    "NOW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREVIOUS",
        "THIS",
        "LAST",
        "NEXT",
        "NOW",
    )
)


def serialize_json(value: TopicRelativeDateFilterFunction) -> str:
    return value


def deserialize_json(data: str) -> TopicRelativeDateFilterFunction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TopicRelativeDateFilterFunction value: {data!r}"
        )
    return cast(TopicRelativeDateFilterFunction, data)
