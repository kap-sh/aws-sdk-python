"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationBillingRequestsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.caller_role
    import aws_sdk_ec2.types.capacity_reservation_id_set
    import aws_sdk_ec2.types.describe_capacity_reservation_billing_requests_request_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeCapacityReservationBillingRequestsRequest(TypedDict):
    capacity_reservation_ids: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id_set.CapacityReservationIdSet"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    role: NotRequired["aws_sdk_ec2.types.caller_role.CallerRole"]
    """<p>Specify one of the following:</p> <ul> <li> <p> <code>odcr-owner</code> - If you are the Capacity Reservation owner, specify this value to view requests that you have initiated. Not supported with the <code>requested-by</code> filter.</p> </li> <li> <p> <code>unused-reservation-billing-owner</code> - If you are the consumer account, specify this value to view requests that have been sent to you. Not supported with the <code>unused-reservation-billing-owner</code> filter.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_capacity_reservation_billing_requests_request_max_results.DescribeCapacityReservationBillingRequestsRequestMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>status</code> - The state of the request (<code>pending</code> | <code>accepted</code> | <code>rejected</code> | <code>cancelled</code> | <code>revoked</code> | <code>expired</code>).</p> </li> <li> <p> <code>requested-by</code> - The account ID of the Capacity Reservation owner that initiated the request. Not supported if you specify <code>requested-by</code> for <b>Role</b>.</p> </li> <li> <p> <code>unused-reservation-billing-owner</code> - The ID of the consumer account to which the request was sent. Not supported if you specify <code>unused-reservation-billing-owner</code> for <b>Role</b>.</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
