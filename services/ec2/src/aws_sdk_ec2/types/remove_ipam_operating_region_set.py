"""Generated from Smithy shape ``com.amazonaws.ec2#RemoveIpamOperatingRegionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.remove_ipam_operating_region

RemoveIpamOperatingRegionSet: TypeAlias = list[
    "aws_sdk_ec2.types.remove_ipam_operating_region.RemoveIpamOperatingRegion"
]
