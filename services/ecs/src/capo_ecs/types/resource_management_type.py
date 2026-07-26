"""Generated from Smithy shape ``com.amazonaws.ecs#ResourceManagementType``."""

from typing import Literal, TypeAlias, cast

ResourceManagementType: TypeAlias = Literal[
    "CUSTOMER",
    "ECS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceManagementType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceManagementType:
    return cast(ResourceManagementType, data)
