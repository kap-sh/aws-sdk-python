"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRouteServerPeerRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.route_server_bgp_options_request
    import aws_sdk_ec2.types.route_server_endpoint_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateRouteServerPeerRequest(TypedDict):
    route_server_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.route_server_endpoint_id.RouteServerEndpointId"
    ]
    """<p>The ID of the route server endpoint for which to create a peer.</p>"""
    peer_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address of the peer device.</p>"""
    bgp_options: NotRequired[
        "aws_sdk_ec2.types.route_server_bgp_options_request.RouteServerBgpOptionsRequest"
    ]
    """<p>The BGP options for the peer, including ASN (Autonomous System Number) and BFD (Bidrectional Forwarding Detection) settings.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the route server peer during creation.</p>"""
