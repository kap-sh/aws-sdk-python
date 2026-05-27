"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesModificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_modification

ReservedInstancesModificationList: TypeAlias = list[
    "aws_sdk_ec2.types.reserved_instances_modification.ReservedInstancesModification"
]
