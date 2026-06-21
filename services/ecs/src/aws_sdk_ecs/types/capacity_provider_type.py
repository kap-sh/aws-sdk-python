"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderType``."""

from typing import Literal, TypeAlias, cast

CapacityProviderType: TypeAlias = Literal[
    "EC2_AUTOSCALING",
    "MANAGED_INSTANCES",
    "FARGATE",
    "FARGATE_SPOT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityProviderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityProviderType:
    return cast(CapacityProviderType, data)
