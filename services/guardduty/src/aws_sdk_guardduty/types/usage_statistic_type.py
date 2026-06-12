"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageStatisticType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

UsageStatisticType: TypeAlias = Literal[
    "SUM_BY_ACCOUNT",
    "SUM_BY_DATA_SOURCE",
    "SUM_BY_RESOURCE",
    "TOP_RESOURCES",
    "SUM_BY_FEATURES",
    "TOP_ACCOUNTS_BY_FEATURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUM_BY_ACCOUNT",
        "SUM_BY_DATA_SOURCE",
        "SUM_BY_RESOURCE",
        "TOP_RESOURCES",
        "SUM_BY_FEATURES",
        "TOP_ACCOUNTS_BY_FEATURE",
    )
)


def serialize_json(value: UsageStatisticType) -> str:
    return value


def deserialize_json(data: str) -> UsageStatisticType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageStatisticType value: {data!r}")
    return cast(UsageStatisticType, data)
