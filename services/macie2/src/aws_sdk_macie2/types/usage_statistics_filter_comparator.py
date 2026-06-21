"""Generated from Smithy shape ``com.amazonaws.macie2#UsageStatisticsFilterComparator``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: UsageStatisticsFilterComparator) -> str:
    return value


def deserialize_json(data: str) -> UsageStatisticsFilterComparator:
    return cast(UsageStatisticsFilterComparator, data)
