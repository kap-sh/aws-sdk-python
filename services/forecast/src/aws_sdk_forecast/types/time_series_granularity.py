"""Generated from Smithy shape ``com.amazonaws.forecast#TimeSeriesGranularity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

TimeSeriesGranularity: TypeAlias = Literal[
    "ALL",
    "SPECIFIC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "SPECIFIC",
    )
)


def serialize_aws_json_1_1(value: TimeSeriesGranularity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimeSeriesGranularity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeSeriesGranularity value: {data!r}")
    return cast(TimeSeriesGranularity, data)
