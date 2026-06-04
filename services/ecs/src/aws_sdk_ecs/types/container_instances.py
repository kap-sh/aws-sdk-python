"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_instance

ContainerInstances: TypeAlias = list[
    "aws_sdk_ecs.types.container_instance.ContainerInstance"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerInstances) -> list:
    import aws_sdk_ecs.types.container_instance

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.container_instance.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerInstances:
    import aws_sdk_ecs.types.container_instance

    out: ContainerInstances = []
    for item in data:
        out.append(aws_sdk_ecs.types.container_instance.deserialize_aws_json_1_1(item))
    return out
