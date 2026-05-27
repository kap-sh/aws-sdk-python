"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayRouteTableRoute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class TransitGatewayRouteTableRoute(TypedDict):
    destination_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block used for destination matches.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state of the route.</p>"""
    route_origin: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The route origin. The following are the possible values:</p> <ul> <li> <p>static</p> </li> <li> <p>propagated</p> </li> </ul>"""
    prefix_list_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the prefix list.</p>"""
    attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the route attachment.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource for the route attachment.</p>"""
    resource_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource type for the route attachment.</p>"""
