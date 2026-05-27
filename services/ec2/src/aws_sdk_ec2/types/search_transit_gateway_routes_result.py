"""Generated from Smithy shape ``com.amazonaws.ec2#SearchTransitGatewayRoutesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_route_list


class SearchTransitGatewayRoutesResult(TypedDict):
    routes: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_list.TransitGatewayRouteList"
    ]
    """<p>Information about the routes.</p>"""
    additional_routes_available: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether there are additional routes available.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
