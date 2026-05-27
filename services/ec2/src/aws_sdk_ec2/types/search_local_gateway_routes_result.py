"""Generated from Smithy shape ``com.amazonaws.ec2#SearchLocalGatewayRoutesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_list
    import aws_sdk_ec2.types.string


class SearchLocalGatewayRoutesResult(TypedDict):
    routes: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_list.LocalGatewayRouteList"
    ]
    """<p>Information about the routes.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
