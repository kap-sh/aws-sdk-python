"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTaskIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_task_id

ExportTaskIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.export_task_id.ExportTaskId"
]
