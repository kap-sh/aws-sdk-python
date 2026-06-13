"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorSpecifiedAggregation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AuthorSpecifiedAggregation: TypeAlias = Literal[
    "COUNT",
    "DISTINCT_COUNT",
    "MIN",
    "MAX",
    "MEDIAN",
    "SUM",
    "AVERAGE",
    "STDEV",
    "STDEVP",
    "VAR",
    "VARP",
    "PERCENTILE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COUNT",
        "DISTINCT_COUNT",
        "MIN",
        "MAX",
        "MEDIAN",
        "SUM",
        "AVERAGE",
        "STDEV",
        "STDEVP",
        "VAR",
        "VARP",
        "PERCENTILE",
    )
)


def serialize_json(value: AuthorSpecifiedAggregation) -> str:
    return value


def deserialize_json(data: str) -> AuthorSpecifiedAggregation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AuthorSpecifiedAggregation value: {data!r}"
        )
    return cast(AuthorSpecifiedAggregation, data)
