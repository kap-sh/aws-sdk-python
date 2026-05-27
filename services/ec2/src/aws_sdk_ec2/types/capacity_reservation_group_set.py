"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationGroupSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_group

CapacityReservationGroupSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_reservation_group.CapacityReservationGroup"
]
