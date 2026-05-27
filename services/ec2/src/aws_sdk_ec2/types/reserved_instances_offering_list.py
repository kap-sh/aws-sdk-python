"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesOfferingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_offering

ReservedInstancesOfferingList: TypeAlias = list[
    "aws_sdk_ec2.types.reserved_instances_offering.ReservedInstancesOffering"
]
