"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityReservationFleetsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_reservation_fleet_id_set
    import aws_sdk_ec2.types.describe_capacity_reservation_fleets_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeCapacityReservationFleetsRequest(TypedDict):
    capacity_reservation_fleet_ids: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_fleet_id_set.CapacityReservationFleetIdSet"
    ]
    """<p>The IDs of the Capacity Reservation Fleets to describe.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_capacity_reservation_fleets_max_results.DescribeCapacityReservationFleetsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>state</code> - The state of the Fleet (<code>submitted</code> | <code>modifying</code> | <code>active</code> | <code>partially_fulfilled</code> | <code>expiring</code> | <code>expired</code> | <code>cancelling</code> | <code>cancelled</code> | <code>failed</code>).</p> </li> <li> <p> <code>instance-match-criteria</code> - The instance matching criteria for the Fleet. Only <code>open</code> is supported.</p> </li> <li> <p> <code>tenancy</code> - The tenancy of the Fleet (<code>default</code> | <code>dedicated</code>).</p> </li> <li> <p> <code>allocation-strategy</code> - The allocation strategy used by the Fleet. Only <code>prioritized</code> is supported.</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
