"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRouteServerPeersRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.route_server_max_results
    import aws_sdk_ec2.types.route_server_peer_ids_list
    import aws_sdk_ec2.types.string


class DescribeRouteServerPeersRequest(TypedDict):
    route_server_peer_ids: NotRequired[
        "aws_sdk_ec2.types.route_server_peer_ids_list.RouteServerPeerIdsList"
    ]
    """<p>The IDs of the route server peers to describe.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.route_server_max_results.RouteServerMaxResults"
    ]
    """<p>The maximum number of results to return with a single call.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters to apply to the describe request.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
