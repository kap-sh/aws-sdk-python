"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAvailabilityZoneIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id

ClientVpnAvailabilityZoneIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
]
