"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesModificationIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_modification_id

ReservedInstancesModificationIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.reserved_instances_modification_id.ReservedInstancesModificationId"
]
