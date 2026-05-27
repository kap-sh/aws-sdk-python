"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolAllocationResourceType``."""

from typing import Literal, TypeAlias

IpamPoolAllocationResourceType: TypeAlias = Literal[
    "ipam-pool",
    "vpc",
    "ec2-public-ipv4-pool",
    "custom",
    "subnet",
    "eip",
    "anycast-ip-list",
]
