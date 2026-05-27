"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesOfferingIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_offering_id

ReservedInstancesOfferingIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.reserved_instances_offering_id.ReservedInstancesOfferingId"
]
