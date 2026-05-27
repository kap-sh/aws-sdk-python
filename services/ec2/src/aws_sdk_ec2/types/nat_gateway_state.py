"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayState``."""

from typing import Literal, TypeAlias

NatGatewayState: TypeAlias = Literal[
    "pending",
    "failed",
    "available",
    "deleting",
    "deleted",
]
