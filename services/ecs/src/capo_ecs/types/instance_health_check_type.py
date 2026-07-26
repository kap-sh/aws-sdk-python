"""Generated from Smithy shape ``com.amazonaws.ecs#InstanceHealthCheckType``."""

from typing import Literal, TypeAlias, cast

InstanceHealthCheckType: TypeAlias = Literal[
    "CONTAINER_RUNTIME",
    "ACCELERATED_COMPUTE",
    "DAEMON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceHealthCheckType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceHealthCheckType:
    return cast(InstanceHealthCheckType, data)
