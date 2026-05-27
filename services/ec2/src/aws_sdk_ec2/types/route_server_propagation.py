"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPropagation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_id
    import aws_sdk_ec2.types.route_server_propagation_state
    import aws_sdk_ec2.types.route_table_id


class RouteServerPropagation(TypedDict):
    route_server_id: NotRequired["aws_sdk_ec2.types.route_server_id.RouteServerId"]
    """<p>The ID of the route server configured for route propagation.</p>"""
    route_table_id: NotRequired["aws_sdk_ec2.types.route_table_id.RouteTableId"]
    """<p>The ID of the route table configured for route server propagation.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.route_server_propagation_state.RouteServerPropagationState"
    ]
    """<p>The current state of route propagation.</p>"""
