"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockOfferingsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_capacity_block_offerings_max_results
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class DescribeCapacityBlockOfferingsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of instance for which the Capacity Block offering reserves capacity.</p>"""
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances for which to reserve capacity. Each Capacity Block can have up to 64 instances, and you can have up to 256 instances across Capacity Blocks.</p>"""
    start_date_range: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The earliest start date for the Capacity Block offering.</p>"""
    end_date_range: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The latest end date for the Capacity Block offering.</p>"""
    capacity_duration_hours: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The reservation duration for the Capacity Block, in hours. You must specify the duration in 1-day increments up 14 days, and in 7-day increments up to 182 days.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_capacity_block_offerings_max_results.DescribeCapacityBlockOfferingsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    ultraserver_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The EC2 UltraServer type of the Capacity Block offerings.</p>"""
    ultraserver_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of EC2 UltraServers in the offerings.</p>"""
    all_availability_zones: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Include all Availability Zones and Local Zones, regardless of your opt-in status. If you do not use this parameter, the results include available offerings from all Availability Zones in the Amazon Web Services Region and Local Zones you are opted into. </p>"""
