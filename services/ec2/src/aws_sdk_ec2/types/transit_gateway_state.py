"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayState``."""

from typing import Literal, TypeAlias

TransitGatewayState: TypeAlias = Literal[
    "pending",
    "available",
    "modifying",
    "deleting",
    "deleted",
]
