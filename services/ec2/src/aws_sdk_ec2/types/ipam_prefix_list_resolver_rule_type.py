"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleType``."""

from typing import Literal, TypeAlias

IpamPrefixListResolverRuleType: TypeAlias = Literal[
    "static-cidr",
    "ipam-resource-cidr",
    "ipam-pool-cidr",
]
