"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerRoute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.as_path
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.route_server_endpoint_id
    import aws_sdk_ec2.types.route_server_peer_id
    import aws_sdk_ec2.types.route_server_route_installation_details
    import aws_sdk_ec2.types.route_server_route_status
    import aws_sdk_ec2.types.string


class RouteServerRoute(TypedDict):
    route_server_endpoint_id: NotRequired[
        "aws_sdk_ec2.types.route_server_endpoint_id.RouteServerEndpointId"
    ]
    """<p>The ID of the route server endpoint that received this route.</p>"""
    route_server_peer_id: NotRequired[
        "aws_sdk_ec2.types.route_server_peer_id.RouteServerPeerId"
    ]
    """<p>The ID of the route server peer that advertised this route.</p>"""
    route_installation_details: NotRequired[
        "aws_sdk_ec2.types.route_server_route_installation_details.RouteServerRouteInstallationDetails"
    ]
    """<p>Details about the installation status of this route in route tables.</p>"""
    route_status: NotRequired[
        "aws_sdk_ec2.types.route_server_route_status.RouteServerRouteStatus"
    ]
    """<p>The current status of the route in the routing database. Values are <code>in-rib</code> or <code>in-fib</code> depending on if the routes are in the RIB or the FIB database.</p> <p>The <a href=\"https://en.wikipedia.org/wiki/Routing_table\">Routing Information Base (RIB)</a> serves as a database that stores all the routing information and network topology data collected by a router or routing system, such as routes learned from BGP peers. The RIB is constantly updated as new routing information is received or existing routes change. This ensures that the route server always has the most current view of the network topology and can make optimal routing decisions.</p> <p>The <a href=\"https://en.wikipedia.org/wiki/Forwarding_information_base\">Forwarding Information Base (FIB)</a> serves as a forwarding table for what route server has determined are the best-path routes in the RIB after evaluating all available routing information and policies. The FIB routes are installed on the route tables. The FIB is recomputed whenever there are changes to the RIB.</p>"""
    prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination CIDR block of the route.</p>"""
    as_paths: NotRequired["aws_sdk_ec2.types.as_path.AsPath"]
    """<p>The AS path attributes of the BGP route.</p>"""
    med: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Multi-Exit Discriminator (MED) value of the BGP route.</p>"""
    next_hop_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address for the next hop.</p>"""
