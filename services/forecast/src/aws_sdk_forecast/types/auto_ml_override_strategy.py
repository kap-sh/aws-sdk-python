"""Generated from Smithy shape ``com.amazonaws.forecast#AutoMLOverrideStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_forecast.errors import DeserializationError

AutoMLOverrideStrategy: TypeAlias = Literal[
    "LatencyOptimized",
    "AccuracyOptimized",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LatencyOptimized",
        "AccuracyOptimized",
    )
)


def serialize_aws_json_1_1(value: AutoMLOverrideStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLOverrideStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLOverrideStrategy value: {data!r}")
    return cast(AutoMLOverrideStrategy, data)
