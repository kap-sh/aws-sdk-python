"""Generated from Smithy shape ``com.amazonaws.ec2#IpamOperatingRegionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_operating_region

IpamOperatingRegionSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_operating_region.IpamOperatingRegion"
]
