"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_instance

ContainerInstances: TypeAlias = list[
    "aws_sdk_ecs.types.container_instance.ContainerInstance"
]
