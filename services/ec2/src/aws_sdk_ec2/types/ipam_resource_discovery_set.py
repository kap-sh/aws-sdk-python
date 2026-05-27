"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceDiscoverySet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_discovery

IpamResourceDiscoverySet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_resource_discovery.IpamResourceDiscovery"
]
