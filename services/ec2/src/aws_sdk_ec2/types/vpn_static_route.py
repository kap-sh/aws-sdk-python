"""Generated from Smithy shape ``com.amazonaws.ec2#VpnStaticRoute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_state
    import aws_sdk_ec2.types.vpn_static_route_source


class VpnStaticRoute(TypedDict):
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block associated with the local subnet of the customer data center.</p>"""
    source: NotRequired[
        "aws_sdk_ec2.types.vpn_static_route_source.VpnStaticRouteSource"
    ]
    """<p>Indicates how the routes were provided.</p>"""
    state: NotRequired["aws_sdk_ec2.types.vpn_state.VpnState"]
    """<p>The current state of the static route.</p>"""
