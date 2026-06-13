"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicSortDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TopicSortDirection: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASCENDING",
        "DESCENDING",
    )
)


def serialize_json(value: TopicSortDirection) -> str:
    return value


def deserialize_json(data: str) -> TopicSortDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopicSortDirection value: {data!r}")
    return cast(TopicSortDirection, data)
