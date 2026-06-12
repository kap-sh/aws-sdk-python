"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#MetricStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

MetricStatistic: TypeAlias = Literal[
    "Average",
    "Minimum",
    "Maximum",
    "SampleCount",
    "Sum",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Average",
        "Minimum",
        "Maximum",
        "SampleCount",
        "Sum",
    )
)


def serialize_aws_json_1_1(value: MetricStatistic) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricStatistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricStatistic value: {data!r}")
    return cast(MetricStatistic, data)
