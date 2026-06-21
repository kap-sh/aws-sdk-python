"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerCondition``."""

from typing import Literal, TypeAlias, cast

ContainerCondition: TypeAlias = Literal[
    "START",
    "COMPLETE",
    "SUCCESS",
    "HEALTHY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerCondition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerCondition:
    return cast(ContainerCondition, data)
