"""Generated from Smithy shape ``com.amazonaws.ec2#InterruptibleCapacityReservationAllocationStatus``."""

from typing import Literal, TypeAlias

InterruptibleCapacityReservationAllocationStatus: TypeAlias = Literal[
    "pending",
    "active",
    "updating",
    "canceling",
    "canceled",
    "failed",
]
