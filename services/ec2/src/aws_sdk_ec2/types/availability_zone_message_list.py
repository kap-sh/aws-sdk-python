"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_message

AvailabilityZoneMessageList: TypeAlias = list[
    "aws_sdk_ec2.types.availability_zone_message.AvailabilityZoneMessage"
]
