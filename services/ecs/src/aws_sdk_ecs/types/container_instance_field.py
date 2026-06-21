"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstanceField``."""

from typing import Literal, TypeAlias, cast

ContainerInstanceField: TypeAlias = Literal[
    "TAGS",
    "CONTAINER_INSTANCE_HEALTH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerInstanceField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContainerInstanceField:
    return cast(ContainerInstanceField, data)
