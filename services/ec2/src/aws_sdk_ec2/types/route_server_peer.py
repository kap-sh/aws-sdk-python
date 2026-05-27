"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPeer``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.route_server_bfd_status
    import aws_sdk_ec2.types.route_server_bgp_options
    import aws_sdk_ec2.types.route_server_bgp_status
    import aws_sdk_ec2.types.route_server_endpoint_id
    import aws_sdk_ec2.types.route_server_id
    import aws_sdk_ec2.types.route_server_peer_id
    import aws_sdk_ec2.types.route_server_peer_state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_id
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_id


class RouteServerPeer(TypedDict):
    route_server_peer_id: NotRequired[
        "aws_sdk_ec2.types.route_server_peer_id.RouteServerPeerId"
    ]
    """<p>The unique identifier of the route server peer.</p>"""
    route_server_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.route_server_endpoint_id.RouteServerEndpointId"
    ]
    """<p>The ID of the route server endpoint associated with this peer.</p>"""
    route_server_id: NotRequired["aws_sdk_ec2.types.route_server_id.RouteServerId"]
    """<p>The ID of the route server associated with this peer.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC containing the route server peer.</p>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet containing the route server peer.</p>"""
    state: NotRequired["aws_sdk_ec2.types.route_server_peer_state.RouteServerPeerState"]
    """<p>The current state of the route server peer.</p>"""
    failure_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for any failure in peer creation or operation.</p>"""
    endpoint_eni_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the Elastic network interface for the route server endpoint.</p>"""
    endpoint_eni_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address of the Elastic network interface for the route server endpoint.</p>"""
    peer_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address of the peer device.</p>"""
    bgp_options: NotRequired[
        "aws_sdk_ec2.types.route_server_bgp_options.RouteServerBgpOptions"
    ]
    """<p>The BGP configuration options for this peer, including ASN (Autonomous System Number) and BFD (Bidrectional Forwarding Detection) settings.</p>"""
    bgp_status: NotRequired[
        "aws_sdk_ec2.types.route_server_bgp_status.RouteServerBgpStatus"
    ]
    """<p>The current status of the BGP session with this peer.</p>"""
    bfd_status: NotRequired[
        "aws_sdk_ec2.types.route_server_bfd_status.RouteServerBfdStatus"
    ]
    """<p>The current status of the BFD session with this peer.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the route server peer.</p>"""
