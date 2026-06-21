"""Generated from Smithy shape ``com.amazonaws.connect#IntervalPeriod``."""

from typing import Literal, TypeAlias, cast

IntervalPeriod: TypeAlias = Literal[
    "FIFTEEN_MIN",
    "THIRTY_MIN",
    "HOUR",
    "DAY",
    "WEEK",
    "TOTAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: IntervalPeriod) -> str:
    return value


def deserialize_json(data: str) -> IntervalPeriod:
    return cast(IntervalPeriod, data)
