"""Generated from Smithy shape ``com.amazonaws.macie2#UsageStatisticsSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The field to use to sort the results of a query for Amazon Macie account quotas and usage data. Valid values are:</p>"""
UsageStatisticsSortKey: TypeAlias = Literal[
    "accountId",
    "total",
    "serviceLimitValue",
    "freeTrialStartDate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "accountId",
        "total",
        "serviceLimitValue",
        "freeTrialStartDate",
    )
)


def serialize_json(value: UsageStatisticsSortKey) -> str:
    return value


def deserialize_json(data: str) -> UsageStatisticsSortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageStatisticsSortKey value: {data!r}")
    return cast(UsageStatisticsSortKey, data)
