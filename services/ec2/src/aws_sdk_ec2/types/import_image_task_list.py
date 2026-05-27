"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_image_task

ImportImageTaskList: TypeAlias = list[
    "aws_sdk_ec2.types.import_image_task.ImportImageTask"
]
