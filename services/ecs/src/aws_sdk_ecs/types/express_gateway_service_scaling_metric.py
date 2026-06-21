"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceScalingMetric``."""

from typing import Literal, TypeAlias, cast

ExpressGatewayServiceScalingMetric: TypeAlias = Literal[
    "AVERAGE_CPU",
    "AVERAGE_MEMORY",
    "REQUEST_COUNT_PER_TARGET",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceScalingMetric) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExpressGatewayServiceScalingMetric:
    return cast(ExpressGatewayServiceScalingMetric, data)
