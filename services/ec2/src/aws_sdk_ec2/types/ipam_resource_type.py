"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceType``."""

from typing import Literal, TypeAlias

IpamResourceType: TypeAlias = Literal[
    "vpc",
    "subnet",
    "eip",
    "public-ipv4-pool",
    "ipv6-pool",
    "eni",
    "anycast-ip-list",
]
