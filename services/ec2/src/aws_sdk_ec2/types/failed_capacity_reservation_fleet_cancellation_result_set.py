"""Generated from Smithy shape ``com.amazonaws.ec2#FailedCapacityReservationFleetCancellationResultSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result

FailedCapacityReservationFleetCancellationResultSet: TypeAlias = list[
    "aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result.FailedCapacityReservationFleetCancellationResult"
]
