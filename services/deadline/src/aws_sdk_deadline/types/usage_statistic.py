"""Generated from Smithy shape ``com.amazonaws.deadline#UsageStatistic``."""

from typing import Literal, TypeAlias, cast

UsageStatistic: TypeAlias = Literal[
    "SUM",
    "MIN",
    "MAX",
    "AVG",
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageStatistic) -> str:
    return value


def deserialize_json(data: str) -> UsageStatistic:
    return cast(UsageStatistic, data)
