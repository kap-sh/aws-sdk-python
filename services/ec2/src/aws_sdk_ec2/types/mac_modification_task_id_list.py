"""Generated from Smithy shape ``com.amazonaws.ec2#MacModificationTaskIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_modification_task_id

MacModificationTaskIdList: TypeAlias = list[
    "aws_sdk_ec2.types.mac_modification_task_id.MacModificationTaskId"
]
