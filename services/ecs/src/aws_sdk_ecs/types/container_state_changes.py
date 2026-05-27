"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerStateChanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.container_state_change

ContainerStateChanges: TypeAlias = list[
    "aws_sdk_ecs.types.container_state_change.ContainerStateChange"
]
