"""Generated from Smithy shape ``com.amazonaws.ec2#AddIpamOperatingRegionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_ipam_operating_region

AddIpamOperatingRegionSet: TypeAlias = list[
    "aws_sdk_ec2.types.add_ipam_operating_region.AddIpamOperatingRegion"
]
