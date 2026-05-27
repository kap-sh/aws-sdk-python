"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationBillingRequestStatus``."""

from typing import Literal, TypeAlias

CapacityReservationBillingRequestStatus: TypeAlias = Literal[
    "pending",
    "accepted",
    "rejected",
    "cancelled",
    "revoked",
    "expired",
]
