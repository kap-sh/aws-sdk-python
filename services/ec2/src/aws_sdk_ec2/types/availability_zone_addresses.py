"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_address

AvailabilityZoneAddresses: TypeAlias = list[
    "aws_sdk_ec2.types.availability_zone_address.AvailabilityZoneAddress"
]
