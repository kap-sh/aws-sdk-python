"""Generated from Smithy shape ``com.amazonaws.macie2#UsageStatisticsFilterComparator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The operator to use in a condition that filters the results of a query for Amazon Macie account quotas and usage data. Valid values are:</p>"""
UsageStatisticsFilterComparator: TypeAlias = Literal[
    "GT",
    "GTE",
    "LT",
    "LTE",
    "EQ",
    "NE",
    "CONTAINS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GT",
        "GTE",
        "LT",
        "LTE",
        "EQ",
        "NE",
        "CONTAINS",
    )
)


def serialize_json(value: UsageStatisticsFilterComparator) -> str:
    return value


def deserialize_json(data: str) -> UsageStatisticsFilterComparator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UsageStatisticsFilterComparator value: {data!r}"
        )
    return cast(UsageStatisticsFilterComparator, data)
