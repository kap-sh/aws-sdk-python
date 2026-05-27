"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerDependencies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_dependency

ContainerDependencies: TypeAlias = list[
    "aws_sdk_ecs.types.container_dependency.ContainerDependency"
]
