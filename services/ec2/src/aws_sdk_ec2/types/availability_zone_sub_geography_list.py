"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneSubGeographyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_sub_geography

AvailabilityZoneSubGeographyList: TypeAlias = list[
    "aws_sdk_ec2.types.availability_zone_sub_geography.AvailabilityZoneSubGeography"
]
