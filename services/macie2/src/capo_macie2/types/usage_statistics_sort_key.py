"""Generated from Smithy shape ``com.amazonaws.macie2#UsageStatisticsSortKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The field to use to sort the results of a query for Amazon Macie account quotas and usage data. Valid values are:</p>"""
UsageStatisticsSortKey: TypeAlias = Literal[
    "accountId",
    "total",
    "serviceLimitValue",
    "freeTrialStartDate",
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageStatisticsSortKey) -> str:
    return value


def deserialize_json(data: str) -> UsageStatisticsSortKey:
    return cast(UsageStatisticsSortKey, data)
