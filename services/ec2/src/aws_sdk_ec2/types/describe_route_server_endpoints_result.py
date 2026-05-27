"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRouteServerEndpointsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_endpoints_list
    import aws_sdk_ec2.types.string


class DescribeRouteServerEndpointsResult(TypedDict):
    route_server_endpoints: NotRequired[
        "aws_sdk_ec2.types.route_server_endpoints_list.RouteServerEndpointsList"
    ]
    """<p>Information about the described route server endpoints.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
