"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerDependencies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_dependency

ContainerDependencies: TypeAlias = list[
    "aws_sdk_ecs.types.container_dependency.ContainerDependency"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDependencies) -> list:
    import aws_sdk_ecs.types.container_dependency

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.container_dependency.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerDependencies:
    import aws_sdk_ecs.types.container_dependency

    out: ContainerDependencies = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.container_dependency.deserialize_aws_json_1_1(item)
        )
    return out
