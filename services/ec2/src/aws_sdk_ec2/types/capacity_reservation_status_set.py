"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_status

CapacityReservationStatusSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_reservation_status.CapacityReservationStatus"
]
