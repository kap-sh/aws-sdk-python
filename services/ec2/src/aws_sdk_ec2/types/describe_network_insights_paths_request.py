"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInsightsPathsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.network_insights_max_results
    import aws_sdk_ec2.types.network_insights_path_id_list
    import aws_sdk_ec2.types.next_token


class DescribeNetworkInsightsPathsRequest(TypedDict):
    network_insights_path_ids: NotRequired[
        "aws_sdk_ec2.types.network_insights_path_id_list.NetworkInsightsPathIdList"
    ]
    """<p>The IDs of the paths.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters. The following are the possible values:</p> <ul> <li> <p>destination - The ID of the resource.</p> </li> <li> <p>filter-at-source.source-address - The source IPv4 address at the source.</p> </li> <li> <p>filter-at-source.source-port-range - The source port range at the source.</p> </li> <li> <p>filter-at-source.destination-address - The destination IPv4 address at the source.</p> </li> <li> <p>filter-at-source.destination-port-range - The destination port range at the source.</p> </li> <li> <p>filter-at-destination.source-address - The source IPv4 address at the destination.</p> </li> <li> <p>filter-at-destination.source-port-range - The source port range at the destination.</p> </li> <li> <p>filter-at-destination.destination-address - The destination IPv4 address at the destination.</p> </li> <li> <p>filter-at-destination.destination-port-range - The destination port range at the destination.</p> </li> <li> <p>protocol - The protocol.</p> </li> <li> <p>source - The ID of the resource.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.network_insights_max_results.NetworkInsightsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
