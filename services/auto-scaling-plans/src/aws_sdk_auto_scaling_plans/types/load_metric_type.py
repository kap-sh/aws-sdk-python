"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#LoadMetricType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling_plans.errors import DeserializationError

LoadMetricType: TypeAlias = Literal[
    "ASGTotalCPUUtilization",
    "ASGTotalNetworkIn",
    "ASGTotalNetworkOut",
    "ALBTargetGroupRequestCount",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASGTotalCPUUtilization",
        "ASGTotalNetworkIn",
        "ASGTotalNetworkOut",
        "ALBTargetGroupRequestCount",
    )
)


def serialize_aws_json_1_1(value: LoadMetricType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadMetricType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoadMetricType value: {data!r}")
    return cast(LoadMetricType, data)
