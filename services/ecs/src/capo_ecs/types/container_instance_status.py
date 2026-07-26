"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstanceStatus``."""

from typing import Literal, TypeAlias, cast

ContainerInstanceStatus: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
    "REGISTERING",
    "DEREGISTERING",
    "REGISTRATION_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerInstanceStatus:
    return cast(ContainerInstanceStatus, data)
