"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRootVolumeTasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.replace_root_volume_task

ReplaceRootVolumeTasks: TypeAlias = list[
    "aws_sdk_ec2.types.replace_root_volume_task.ReplaceRootVolumeTask"
]
