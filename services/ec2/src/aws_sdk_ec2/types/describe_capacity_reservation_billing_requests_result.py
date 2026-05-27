"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationBillingRequestsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_billing_request_set
    import aws_sdk_ec2.types.string


class DescribeCapacityReservationBillingRequestsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    capacity_reservation_billing_requests: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_billing_request_set.CapacityReservationBillingRequestSet"
    ]
    """<p>Information about the request.</p>"""
