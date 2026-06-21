"""Generated from Smithy shape ``com.amazonaws.iotwireless#AggregationPeriod``."""

from typing import Literal, TypeAlias, cast

AggregationPeriod: TypeAlias = Literal[
    "OneHour",
    "OneDay",
    "OneWeek",
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationPeriod) -> str:
    return value


def deserialize_json(data: str) -> AggregationPeriod:
    return cast(AggregationPeriod, data)
