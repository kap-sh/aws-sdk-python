"""Generated from Smithy shape ``com.amazonaws.backup#AggregationPeriod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

AggregationPeriod: TypeAlias = Literal[
    "ONE_DAY",
    "SEVEN_DAYS",
    "FOURTEEN_DAYS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONE_DAY",
        "SEVEN_DAYS",
        "FOURTEEN_DAYS",
    )
)


def serialize_json(value: AggregationPeriod) -> str:
    return value


def deserialize_json(data: str) -> AggregationPeriod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AggregationPeriod value: {data!r}")
    return cast(AggregationPeriod, data)
