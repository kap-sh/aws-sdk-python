"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayApplianceState``."""

from typing import Literal, TypeAlias

NatGatewayApplianceState: TypeAlias = Literal[
    "attaching",
    "attached",
    "detaching",
    "detached",
    "attach-failed",
    "detach-failed",
]
