"""Generated from Smithy shape ``com.amazonaws.lightsail#ContainerServiceMetricName``."""

from typing import Literal, TypeAlias, cast

ContainerServiceMetricName: TypeAlias = Literal[
    "CPUUtilization",
    "MemoryUtilization",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerServiceMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerServiceMetricName:
    return cast(ContainerServiceMetricName, data)
