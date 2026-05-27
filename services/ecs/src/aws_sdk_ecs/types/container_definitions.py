"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_definition

ContainerDefinitions: TypeAlias = list[
    "aws_sdk_ecs.types.container_definition.ContainerDefinition"
]
