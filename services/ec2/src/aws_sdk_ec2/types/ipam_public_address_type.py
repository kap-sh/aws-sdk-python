"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPublicAddressType``."""

from typing import Literal, TypeAlias

IpamPublicAddressType: TypeAlias = Literal[
    "service-managed-ip",
    "service-managed-byoip",
    "amazon-owned-eip",
    "amazon-owned-contig",
    "byoip",
    "ec2-public-ip",
    "anycast-ip-list-ip",
]
