"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#MetricAggregationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_auto_scaling.errors import DeserializationError

MetricAggregationType: TypeAlias = Literal[
    "Average",
    "Minimum",
    "Maximum",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Average",
        "Minimum",
        "Maximum",
    )
)


def serialize_aws_json_1_1(value: MetricAggregationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricAggregationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricAggregationType value: {data!r}")
    return cast(MetricAggregationType, data)
