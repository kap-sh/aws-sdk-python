"""Generated from Smithy shape ``com.amazonaws.ec2#DisableRouteServerPropagationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_propagation


class DisableRouteServerPropagationResult(TypedDict):
    route_server_propagation: NotRequired[
        "aws_sdk_ec2.types.route_server_propagation.RouteServerPropagation"
    ]
    """<p>Information about the disabled route server propagation.</p>"""
