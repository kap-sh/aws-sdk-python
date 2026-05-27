"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationBillingRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.account_id
    import aws_sdk_ec2.types.capacity_reservation_billing_request_status
    import aws_sdk_ec2.types.capacity_reservation_info
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class CapacityReservationBillingRequest(TypedDict):
    capacity_reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation.</p>"""
    requested_by: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that initiated the request.</p>"""
    unused_reservation_billing_owner_id: NotRequired[
        "aws_sdk_ec2.types.account_id.AccountID"
    ]
    """<p>The ID of the Amazon Web Services account to which the request was sent.</p>"""
    last_update_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time, in UTC time format, at which the request was initiated.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_billing_request_status.CapacityReservationBillingRequestStatus"
    ]
    """<p>The status of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/view-billing-transfers.html\"> View billing assignment requests for a shared Amazon EC2 Capacity Reservation</a>.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Information about the status.</p>"""
    capacity_reservation_info: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_info.CapacityReservationInfo"
    ]
    """<p>Information about the Capacity Reservation.</p>"""
