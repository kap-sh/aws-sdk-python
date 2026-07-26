"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageStatisticType``."""

from typing import Literal, TypeAlias, cast

UsageStatisticType: TypeAlias = Literal[
    "SUM_BY_ACCOUNT",
    "SUM_BY_DATA_SOURCE",
    "SUM_BY_RESOURCE",
    "TOP_RESOURCES",
    "SUM_BY_FEATURES",
    "TOP_ACCOUNTS_BY_FEATURE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageStatisticType) -> str:
    return value


def deserialize_json(data: str) -> UsageStatisticType:
    return cast(UsageStatisticType, data)
