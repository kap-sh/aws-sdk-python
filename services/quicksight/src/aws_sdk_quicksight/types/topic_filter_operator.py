"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TopicFilterOperator: TypeAlias = Literal[
    "StringEquals",
    "StringLike",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "StringEquals",
        "StringLike",
    )
)


def serialize_json(value: TopicFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> TopicFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopicFilterOperator value: {data!r}")
    return cast(TopicFilterOperator, data)
