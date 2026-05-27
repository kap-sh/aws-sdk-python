"""Generated from Smithy shape ``com.amazonaws.ec2#GetRouteServerRoutingDatabaseResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.route_server_route_list
    import aws_sdk_ec2.types.string


class GetRouteServerRoutingDatabaseResult(TypedDict):
    are_routes_persisted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether routes are being persisted in the routing database.</p>"""
    routes: NotRequired[
        "aws_sdk_ec2.types.route_server_route_list.RouteServerRouteList"
    ]
    """<p>The collection of routes in the route server's routing database.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
