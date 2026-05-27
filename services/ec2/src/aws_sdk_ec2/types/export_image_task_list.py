"""Generated from Smithy shape ``com.amazonaws.ec2#ExportImageTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_image_task

ExportImageTaskList: TypeAlias = list[
    "aws_sdk_ec2.types.export_image_task.ExportImageTask"
]
