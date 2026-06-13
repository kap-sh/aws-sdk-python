"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TopicIRFilterType: TypeAlias = Literal[
    "CATEGORY_FILTER",
    "NUMERIC_EQUALITY_FILTER",
    "NUMERIC_RANGE_FILTER",
    "DATE_RANGE_FILTER",
    "RELATIVE_DATE_FILTER",
    "TOP_BOTTOM_FILTER",
    "EQUALS",
    "RANK_LIMIT_FILTER",
    "ACCEPT_ALL_FILTER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CATEGORY_FILTER",
        "NUMERIC_EQUALITY_FILTER",
        "NUMERIC_RANGE_FILTER",
        "DATE_RANGE_FILTER",
        "RELATIVE_DATE_FILTER",
        "TOP_BOTTOM_FILTER",
        "EQUALS",
        "RANK_LIMIT_FILTER",
        "ACCEPT_ALL_FILTER",
    )
)


def serialize_json(value: TopicIRFilterType) -> str:
    return value


def deserialize_json(data: str) -> TopicIRFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TopicIRFilterType value: {data!r}")
    return cast(TopicIRFilterType, data)
