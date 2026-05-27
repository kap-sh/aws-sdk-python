"""Generated from Smithy shape ``com.amazonaws.ec2#StoreImageTaskResultSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.store_image_task_result

StoreImageTaskResultSet: TypeAlias = list[
    "aws_sdk_ec2.types.store_image_task_result.StoreImageTaskResult"
]
