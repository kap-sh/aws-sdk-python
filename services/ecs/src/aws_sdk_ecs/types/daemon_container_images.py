"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonContainerImages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_container_image

DaemonContainerImages: TypeAlias = list[
    "aws_sdk_ecs.types.daemon_container_image.DaemonContainerImage"
]
