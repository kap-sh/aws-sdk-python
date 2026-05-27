"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayAddressStatus``."""

from typing import Literal, TypeAlias

NatGatewayAddressStatus: TypeAlias = Literal[
    "assigning",
    "unassigning",
    "associating",
    "disassociating",
    "succeeded",
    "failed",
]
