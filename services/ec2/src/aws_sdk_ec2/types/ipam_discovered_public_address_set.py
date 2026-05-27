"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredPublicAddressSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_discovered_public_address

IpamDiscoveredPublicAddressSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_discovered_public_address.IpamDiscoveredPublicAddress"
]
