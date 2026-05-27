"""Generated from Smithy shape ``com.amazonaws.ec2#FleetActivityStatus``."""

from typing import Literal, TypeAlias

FleetActivityStatus: TypeAlias = Literal[
    "error",
    "pending_fulfillment",
    "pending_termination",
    "fulfilled",
]
