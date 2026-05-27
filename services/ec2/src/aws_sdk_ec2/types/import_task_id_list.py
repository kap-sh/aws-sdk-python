"""Generated from Smithy shape ``com.amazonaws.ec2#ImportTaskIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_image_task_id

ImportTaskIdList: TypeAlias = list[
    "aws_sdk_ec2.types.import_image_task_id.ImportImageTaskId"
]
