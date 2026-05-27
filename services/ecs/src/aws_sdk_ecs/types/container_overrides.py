"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_override

ContainerOverrides: TypeAlias = list[
    "aws_sdk_ecs.types.container_override.ContainerOverride"
]
