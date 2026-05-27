"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneGeographyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_geography

AvailabilityZoneGeographyList: TypeAlias = list[
    "aws_sdk_ec2.types.availability_zone_geography.AvailabilityZoneGeography"
]
