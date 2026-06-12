"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceMetricStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ECSServiceMetricStatistic: TypeAlias = Literal[
    "Maximum",
    "Average",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Maximum",
        "Average",
    )
)


def serialize_aws_json_1_0(value: ECSServiceMetricStatistic) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ECSServiceMetricStatistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ECSServiceMetricStatistic value: {data!r}")
    return cast(ECSServiceMetricStatistic, data)
