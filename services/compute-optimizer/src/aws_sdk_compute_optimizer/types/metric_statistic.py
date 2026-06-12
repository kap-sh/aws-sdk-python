"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MetricStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

MetricStatistic: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: MetricStatistic) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MetricStatistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricStatistic value: {data!r}")
    return cast(MetricStatistic, data)
