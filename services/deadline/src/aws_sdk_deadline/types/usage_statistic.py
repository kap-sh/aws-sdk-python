"""Generated from Smithy shape ``com.amazonaws.deadline#UsageStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

UsageStatistic: TypeAlias = Literal[
    "SUM",
    "MIN",
    "MAX",
    "AVG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUM",
        "MIN",
        "MAX",
        "AVG",
    )
)


def serialize_json(value: UsageStatistic) -> str:
    return value


def deserialize_json(data: str) -> UsageStatistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageStatistic value: {data!r}")
    return cast(UsageStatistic, data)
