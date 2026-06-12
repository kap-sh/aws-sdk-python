"""Generated from Smithy shape ``com.amazonaws.connect#IntervalPeriod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

IntervalPeriod: TypeAlias = Literal[
    "FIFTEEN_MIN",
    "THIRTY_MIN",
    "HOUR",
    "DAY",
    "WEEK",
    "TOTAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIFTEEN_MIN",
        "THIRTY_MIN",
        "HOUR",
        "DAY",
        "WEEK",
        "TOTAL",
    )
)


def serialize_json(value: IntervalPeriod) -> str:
    return value


def deserialize_json(data: str) -> IntervalPeriod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntervalPeriod value: {data!r}")
    return cast(IntervalPeriod, data)
