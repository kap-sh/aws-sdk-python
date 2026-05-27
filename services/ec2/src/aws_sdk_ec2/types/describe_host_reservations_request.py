"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostReservationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.host_reservation_id_set
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class DescribeHostReservationsRequest(TypedDict):
    filter: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>instance-family</code> - The instance family (for example, <code>m4</code>).</p> </li> <li> <p> <code>payment-option</code> - The payment option (<code>NoUpfront</code> | <code>PartialUpfront</code> | <code>AllUpfront</code>).</p> </li> <li> <p> <code>state</code> - The state of the reservation (<code>payment-pending</code> | <code>payment-failed</code> | <code>active</code> | <code>retired</code>).</p> </li> <li> <p> <code>tag:<key></code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    host_reservation_id_set: NotRequired[
        "aws_sdk_ec2.types.host_reservation_id_set.HostReservationIdSet"
    ]
    """<p>The host reservation IDs.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned <code>nextToken</code> value. This value can be between 5 and 500. If <code>maxResults</code> is given a larger value than 500, you receive an error.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
