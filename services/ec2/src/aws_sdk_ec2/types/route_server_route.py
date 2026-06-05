"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerRoute``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerRoute, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.RouteServerEndpointId", str(value["route_server_endpoint_id"]))
        )
    if "route_server_peer_id" in value:
        pairs.append(
            (f"{prefix}.RouteServerPeerId", str(value["route_server_peer_id"]))
        )
    if "route_installation_details" in value:
        import aws_sdk_ec2.types.route_server_route_installation_details

        aws_sdk_ec2.types.route_server_route_installation_details.serialize_ec2_query(
            value["route_installation_details"],
            pairs,
            f"{prefix}.RouteInstallationDetailSet",
        )
    if "route_status" in value:
        import aws_sdk_ec2.types.route_server_route_status

        aws_sdk_ec2.types.route_server_route_status.serialize_ec2_query(
            value["route_status"], pairs, f"{prefix}.RouteStatus"
        )
    if "prefix" in value:
        pairs.append((f"{prefix}.Prefix", str(value["prefix"])))
    if "as_paths" in value:
        import aws_sdk_ec2.types.as_path

        aws_sdk_ec2.types.as_path.serialize_ec2_query(
            value["as_paths"], pairs, f"{prefix}.AsPathSet"
        )
    if "med" in value:
        pairs.append((f"{prefix}.Med", str(value["med"])))
    if "next_hop_ip" in value:
        pairs.append((f"{prefix}.NextHopIp", str(value["next_hop_ip"])))


def deserialize_ec2_query(el: Element) -> RouteServerRoute:
    out: RouteServerRoute = {}  # type: ignore[typeddict-item]
    child_route_server_endpoint_id = el.find("RouteServerEndpointId")
    if child_route_server_endpoint_id is not None:
        out["route_server_endpoint_id"] = str(child_route_server_endpoint_id.text or "")
    child_route_server_peer_id = el.find("RouteServerPeerId")
    if child_route_server_peer_id is not None:
        out["route_server_peer_id"] = str(child_route_server_peer_id.text or "")
    if el.find("RouteInstallationDetailSet") is not None:
        import aws_sdk_ec2.types.route_server_route_installation_details

        out["route_installation_details"] = (
            aws_sdk_ec2.types.route_server_route_installation_details.deserialize_ec2_query(
                el, "RouteInstallationDetailSet"
            )
        )
    child_route_status = el.find("RouteStatus")
    if child_route_status is not None:
        import aws_sdk_ec2.types.route_server_route_status

        out["route_status"] = (
            aws_sdk_ec2.types.route_server_route_status.deserialize_ec2_query(
                child_route_status
            )
        )
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    if el.find("AsPathSet") is not None:
        import aws_sdk_ec2.types.as_path

        out["as_paths"] = aws_sdk_ec2.types.as_path.deserialize_ec2_query(
            el, "AsPathSet"
        )
    child_med = el.find("Med")
    if child_med is not None:
        out["med"] = int(child_med.text or "")
    child_next_hop_ip = el.find("NextHopIp")
    if child_next_hop_ip is not None:
        out["next_hop_ip"] = str(child_next_hop_ip.text or "")
    return out
