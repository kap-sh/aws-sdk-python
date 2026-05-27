"""Generated from Smithy shape ``com.amazonaws.ec2#CancelCapacityReservationFleetError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error_code
    import aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error_message


class CancelCapacityReservationFleetError(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error_code.CancelCapacityReservationFleetErrorCode"
    ]
    """<p>The error code.</p>"""
    message: NotRequired[
        "aws_sdk_ec2.types.cancel_capacity_reservation_fleet_error_message.CancelCapacityReservationFleetErrorMessage"
    ]
    """<p>The error message.</p>"""
