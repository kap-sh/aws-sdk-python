"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_definition

ContainerDefinitions: TypeAlias = list[
    "aws_sdk_ecs.types.container_definition.ContainerDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDefinitions) -> list:
    import aws_sdk_ecs.types.container_definition

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.container_definition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ContainerDefinitions:
    import aws_sdk_ecs.types.container_definition

    out: ContainerDefinitions = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.container_definition.deserialize_aws_json_1_1(item)
        )
    return out
