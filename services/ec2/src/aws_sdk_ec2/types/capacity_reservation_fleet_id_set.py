"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationFleetIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_fleet_id

CapacityReservationFleetIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_reservation_fleet_id.CapacityReservationFleetId"
]
