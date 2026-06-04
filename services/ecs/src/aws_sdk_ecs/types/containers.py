"""Generated from Smithy shape ``com.amazonaws.ecs#Containers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container

Containers: TypeAlias = list["aws_sdk_ecs.types.container.Container"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Containers) -> list:
    import aws_sdk_ecs.types.container

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.container.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Containers:
    import aws_sdk_ecs.types.container

    out: Containers = []
    for item in data:
        out.append(aws_sdk_ecs.types.container.deserialize_aws_json_1_1(item))
    return out
