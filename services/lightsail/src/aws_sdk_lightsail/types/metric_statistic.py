"""Generated from Smithy shape ``com.amazonaws.lightsail#MetricStatistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

MetricStatistic: TypeAlias = Literal[
    "Minimum",
    "Maximum",
    "Sum",
    "Average",
    "SampleCount",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Minimum",
        "Maximum",
        "Sum",
        "Average",
        "SampleCount",
    )
)


def serialize_aws_json_1_1(value: MetricStatistic) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricStatistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricStatistic value: {data!r}")
    return cast(MetricStatistic, data)
