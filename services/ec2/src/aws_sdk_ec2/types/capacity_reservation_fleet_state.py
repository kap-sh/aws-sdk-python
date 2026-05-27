"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationFleetState``."""

from typing import Literal, TypeAlias

CapacityReservationFleetState: TypeAlias = Literal[
    "submitted",
    "modifying",
    "active",
    "partially_fulfilled",
    "expiring",
    "expired",
    "cancelling",
    "cancelled",
    "failed",
]
