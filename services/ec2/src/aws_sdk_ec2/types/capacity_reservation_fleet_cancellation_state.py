"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationFleetCancellationState``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_fleet_id
    import aws_sdk_ec2.types.capacity_reservation_fleet_state


class CapacityReservationFleetCancellationState(TypedDict):
    current_fleet_state: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_state.CapacityReservationFleetState"
    ]
    """<p>The current state of the Capacity Reservation Fleet.</p>"""
    previous_fleet_state: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_state.CapacityReservationFleetState"
    ]
    """<p>The previous state of the Capacity Reservation Fleet.</p>"""
    capacity_reservation_fleet_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_id.CapacityReservationFleetId"
    ]
    """<p>The ID of the Capacity Reservation Fleet that was successfully cancelled.</p>"""
