"""Generated from Smithy shape ``com.amazonaws.ecs#TaskVolumeConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_volume_configuration

TaskVolumeConfigurations: TypeAlias = list[
    "aws_sdk_ecs.types.task_volume_configuration.TaskVolumeConfiguration"
]
