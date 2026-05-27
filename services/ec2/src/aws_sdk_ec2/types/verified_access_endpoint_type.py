"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointType``."""

from typing import Literal, TypeAlias

VerifiedAccessEndpointType: TypeAlias = Literal[
    "load-balancer",
    "network-interface",
    "rds",
    "cidr",
]
