"""Generated from Smithy shape ``com.amazonaws.macie2#UsageStatisticsFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The field to use in a condition that filters the results of a query for Amazon Macie account quotas and usage data. Valid values are:</p>"""
UsageStatisticsFilterKey: TypeAlias = Literal[
    "accountId",
    "serviceLimit",
    "freeTrialStartDate",
    "total",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "accountId",
        "serviceLimit",
        "freeTrialStartDate",
        "total",
    )
)


def serialize_json(value: UsageStatisticsFilterKey) -> str:
    return value


def deserialize_json(data: str) -> UsageStatisticsFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageStatisticsFilterKey value: {data!r}")
    return cast(UsageStatisticsFilterKey, data)
