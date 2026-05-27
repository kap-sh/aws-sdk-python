"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRouteServersResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_servers_list
    import aws_sdk_ec2.types.string


class DescribeRouteServersResult(TypedDict):
    route_servers: NotRequired["aws_sdk_ec2.types.route_servers_list.RouteServersList"]
    """<p>Information about the described route servers.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
