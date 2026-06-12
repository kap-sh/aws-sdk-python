"""Generated from Smithy shape ``com.amazonaws.iotwireless#AggregationPeriod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

AggregationPeriod: TypeAlias = Literal[
    "OneHour",
    "OneDay",
    "OneWeek",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OneHour",
        "OneDay",
        "OneWeek",
    )
)


def serialize_json(value: AggregationPeriod) -> str:
    return value


def deserialize_json(data: str) -> AggregationPeriod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AggregationPeriod value: {data!r}")
    return cast(AggregationPeriod, data)
