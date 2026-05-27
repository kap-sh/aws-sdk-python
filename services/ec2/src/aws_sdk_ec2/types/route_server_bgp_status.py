"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerBgpStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_bgp_state


class RouteServerBgpStatus(TypedDict):
    status: NotRequired["aws_sdk_ec2.types.route_server_bgp_state.RouteServerBgpState"]
    """<p>The operational status of the BGP session. The status enables you to monitor session liveness if you lack monitoring on your router/appliance.</p>"""
