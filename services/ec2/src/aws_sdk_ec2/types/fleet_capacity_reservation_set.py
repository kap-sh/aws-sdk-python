"""Generated from Smithy shape ``com.amazonaws.ec2#FleetCapacityReservationSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fleet_capacity_reservation

FleetCapacityReservationSet: TypeAlias = list[
    "aws_sdk_ec2.types.fleet_capacity_reservation.FleetCapacityReservation"
]
