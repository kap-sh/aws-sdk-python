"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedIntancesIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_id

ReservedIntancesIds: TypeAlias = list[
    "aws_sdk_ec2.types.reserved_instances_id.ReservedInstancesId"
]
