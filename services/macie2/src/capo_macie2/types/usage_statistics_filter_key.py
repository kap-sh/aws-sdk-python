"""Generated from Smithy shape ``com.amazonaws.macie2#UsageStatisticsFilterKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The field to use in a condition that filters the results of a query for Amazon Macie account quotas and usage data. Valid values are:</p>"""
UsageStatisticsFilterKey: TypeAlias = Literal[
    "accountId",
    "serviceLimit",
    "freeTrialStartDate",
    "total",
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageStatisticsFilterKey) -> str:
    return value


def deserialize_json(data: str) -> UsageStatisticsFilterKey:
    return cast(UsageStatisticsFilterKey, data)
