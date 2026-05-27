"""Generated from Smithy shape ``com.amazonaws.ec2#CancelCapacityReservationFleetsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state_set
    import aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result_set


class CancelCapacityReservationFleetsResult(TypedDict):
    successful_fleet_cancellations: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_cancellation_state_set.CapacityReservationFleetCancellationStateSet"
    ]
    """<p>Information about the Capacity Reservation Fleets that were successfully cancelled.</p>"""
    failed_fleet_cancellations: NotRequired[
        "aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result_set.FailedCapacityReservationFleetCancellationResultSet"
    ]
    """<p>Information about the Capacity Reservation Fleets that could not be cancelled.</p>"""
