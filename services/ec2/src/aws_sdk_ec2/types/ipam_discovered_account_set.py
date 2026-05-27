"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredAccountSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_discovered_account

IpamDiscoveredAccountSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_discovered_account.IpamDiscoveredAccount"
]
