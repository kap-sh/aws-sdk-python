"""Generated from Smithy shape ``com.amazonaws.ec2#ExportImageTaskIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_image_task_id

ExportImageTaskIdList: TypeAlias = list[
    "aws_sdk_ec2.types.export_image_task_id.ExportImageTaskId"
]
