"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredResourceCidrSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_discovered_resource_cidr

IpamDiscoveredResourceCidrSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_discovered_resource_cidr.IpamDiscoveredResourceCidr"
]
