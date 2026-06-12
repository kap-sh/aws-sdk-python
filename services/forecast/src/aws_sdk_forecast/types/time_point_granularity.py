"""Generated from Smithy shape ``com.amazonaws.forecast#TimePointGranularity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

TimePointGranularity: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: TimePointGranularity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TimePointGranularity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimePointGranularity value: {data!r}")
    return cast(TimePointGranularity, data)
