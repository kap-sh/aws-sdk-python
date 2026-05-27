"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockExtensionHistoryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_id_set
    import aws_sdk_ec2.types.describe_future_capacity_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeCapacityBlockExtensionHistoryRequest(TypedDict):
    capacity_reservation_ids: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id_set.CapacityReservationIdSet"
    ]
    """<p>The IDs of Capacity Block reservations that you want to display the history for.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_future_capacity_max_results.DescribeFutureCapacityMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone of the extension.</p> </li> <li> <p> <code>availability-zone-id</code> - The Availability Zone ID of the extension.</p> </li> <li> <p> <code>capacity-block-extension-offering-id</code> - The ID of the extension offering.</p> </li> <li> <p> <code>capacity-block-extension-status</code> - The status of the extension (<code>payment-pending</code> | <code>payment-failed</code> | <code>payment-succeeded</code>).</p> </li> <li> <p> <code>capacity-reservation-id</code> - The reservation ID of the extension.</p> </li> <li> <p> <code>instance-type</code> - The instance type of the extension.</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
