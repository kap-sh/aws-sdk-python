"""Generated from Smithy shape ``com.amazonaws.ec2#MacModificationTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_modification_task

MacModificationTaskList: TypeAlias = list[
    "aws_sdk_ec2.types.mac_modification_task.MacModificationTask"
]
