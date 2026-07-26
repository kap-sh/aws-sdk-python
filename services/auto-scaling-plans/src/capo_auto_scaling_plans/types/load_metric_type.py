"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#LoadMetricType``."""

from typing import Literal, TypeAlias, cast

LoadMetricType: TypeAlias = Literal[
    "ASGTotalCPUUtilization",
    "ASGTotalNetworkIn",
    "ASGTotalNetworkOut",
    "ALBTargetGroupRequestCount",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadMetricType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadMetricType:
    return cast(LoadMetricType, data)
