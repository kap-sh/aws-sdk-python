"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationFleetCancellationStateSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state

CapacityReservationFleetCancellationStateSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state.CapacityReservationFleetCancellationState"
]
