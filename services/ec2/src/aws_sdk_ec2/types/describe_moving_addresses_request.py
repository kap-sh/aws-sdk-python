"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMovingAddressesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_moving_addresses_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class DescribeMovingAddressesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    public_ips: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>One or more Elastic IP addresses.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>moving-status</code> - The status of the Elastic IP address (<code>MovingToVpc</code> | <code>RestoringToClassic</code>).</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_moving_addresses_max_results.DescribeMovingAddressesMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results of the initial request can be seen by sending another request with the returned <code>NextToken</code> value. This value can be between 5 and 1000; if <code>MaxResults</code> is given a value outside of this range, an error is returned.</p> <p>Default: If no value is provided, the default is 1000.</p>"""
