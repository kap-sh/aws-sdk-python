"""Generated from Smithy shape ``com.amazonaws.backup#AggregationPeriod``."""

from typing import Literal, TypeAlias, cast

AggregationPeriod: TypeAlias = Literal[
    "ONE_DAY",
    "SEVEN_DAYS",
    "FOURTEEN_DAYS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationPeriod) -> str:
    return value


def deserialize_json(data: str) -> AggregationPeriod:
    return cast(AggregationPeriod, data)
