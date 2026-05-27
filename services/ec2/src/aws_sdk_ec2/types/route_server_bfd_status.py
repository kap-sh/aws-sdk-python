"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerBfdStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_bfd_state


class RouteServerBfdStatus(TypedDict):
    status: NotRequired["aws_sdk_ec2.types.route_server_bfd_state.RouteServerBfdState"]
    """<p>The operational status of the BFD session.</p>"""
