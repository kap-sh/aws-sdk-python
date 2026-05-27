"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumeStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_id_string_list


class DescribeVolumeStatusRequest(TypedDict):
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    volume_ids: NotRequired[
        "aws_sdk_ec2.types.volume_id_string_list.VolumeIdStringList"
    ]
    """<p>The IDs of the volumes.</p> <p>Default: Describes all your volumes.</p>"""
    include_managed_resources: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to include managed resources in the output. If this parameter is set to <code>true</code>, the output includes resources that are managed by Amazon Web Services services, even if managed resource visibility is set to hidden.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>action.code</code> - The action code for the event (for example, <code>enable-volume-io</code>).</p> </li> <li> <p> <code>action.description</code> - A description of the action.</p> </li> <li> <p> <code>action.event-id</code> - The event ID associated with the action.</p> </li> <li> <p> <code>availability-zone</code> - The Availability Zone of the instance.</p> </li> <li> <p> <code>event.description</code> - A description of the event.</p> </li> <li> <p> <code>event.event-id</code> - The event ID.</p> </li> <li> <p> <code>event.event-type</code> - The event type (for <code>io-enabled</code>: <code>passed</code> | <code>failed</code>; for <code>io-performance</code>: <code>io-performance:degraded</code> | <code>io-performance:severely-degraded</code> | <code>io-performance:stalled</code>).</p> </li> <li> <p> <code>event.not-after</code> - The latest end time for the event.</p> </li> <li> <p> <code>event.not-before</code> - The earliest start time for the event.</p> </li> <li> <p> <code>volume-status.details-name</code> - The cause for <code>volume-status.status</code> (<code>io-enabled</code> | <code>io-performance</code>).</p> </li> <li> <p> <code>volume-status.details-status</code> - The status of <code>volume-status.details-name</code> (for <code>io-enabled</code>: <code>passed</code> | <code>failed</code>; for <code>io-performance</code>: <code>normal</code> | <code>degraded</code> | <code>severely-degraded</code> | <code>stalled</code>).</p> </li> <li> <p> <code>volume-status.status</code> - The status of the volume (<code>ok</code> | <code>impaired</code> | <code>warning</code> | <code>insufficient-data</code>).</p> </li> </ul>"""
