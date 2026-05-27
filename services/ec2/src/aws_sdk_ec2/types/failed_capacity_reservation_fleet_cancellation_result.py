"""Generated from Smithy shape ``com.amazonaws.ec2#FailedCapacityReservationFleetCancellationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error
    import aws_sdk_ec2.types.capacity_reservation_fleet_id


class FailedCapacityReservationFleetCancellationResult(TypedDict):
    capacity_reservation_fleet_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_id.CapacityReservationFleetId"
    ]
    """<p>The ID of the Capacity Reservation Fleet that could not be cancelled.</p>"""
    cancel_capacity_reservation_fleet_error: NotRequired[
        "aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error.CancelCapacityReservationFleetError"
    ]
    """<p>Information about the Capacity Reservation Fleet cancellation error.</p>"""
