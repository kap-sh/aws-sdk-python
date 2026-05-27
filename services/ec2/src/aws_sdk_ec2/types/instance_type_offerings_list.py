"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeOfferingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type_offering

InstanceTypeOfferingsList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_type_offering.InstanceTypeOffering"
]
