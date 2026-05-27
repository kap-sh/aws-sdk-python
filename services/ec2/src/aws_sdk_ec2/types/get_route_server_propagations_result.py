"""Generated from Smithy shape ``com.amazonaws.ec2#GetRouteServerPropagationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_propagations_list


class GetRouteServerPropagationsResult(TypedDict):
    route_server_propagations: NotRequired[
        "aws_sdk_ec2.types.route_server_propagations_list.RouteServerPropagationsList"
    ]
    """<p>Information about the route propagations for the specified route server.</p>"""
