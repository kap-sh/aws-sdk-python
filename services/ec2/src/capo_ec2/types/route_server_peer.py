"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPeer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.route_server_bfd_status
    import capo_ec2.types.route_server_bgp_options
    import capo_ec2.types.route_server_bgp_status
    import capo_ec2.types.route_server_endpoint_id
    import capo_ec2.types.route_server_id
    import capo_ec2.types.route_server_peer_id
    import capo_ec2.types.route_server_peer_state
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id
    import capo_ec2.types.tag_list
    import capo_ec2.types.vpc_id


class RouteServerPeer(TypedDict, closed=True):
    route_server_peer_id: NotRequired[
        "capo_ec2.types.route_server_peer_id.RouteServerPeerId"
    ]
    """<p>The unique identifier of the route server peer.</p>"""
    route_server_endpoint_id: NotRequired[
        "capo_ec2.types.route_server_endpoint_id.RouteServerEndpointId"
    ]
    """<p>The ID of the route server endpoint associated with this peer.</p>"""
    route_server_id: NotRequired["capo_ec2.types.route_server_id.RouteServerId"]
    """<p>The ID of the route server associated with this peer.</p>"""
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC containing the route server peer.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet containing the route server peer.</p>"""
    state: NotRequired["capo_ec2.types.route_server_peer_state.RouteServerPeerState"]
    """<p>The current state of the route server peer.</p>"""
    failure_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for any failure in peer creation or operation.</p>"""
    endpoint_eni_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the Elastic network interface for the route server endpoint.</p>"""
    endpoint_eni_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address of the Elastic network interface for the route server endpoint.</p>"""
    peer_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address of the peer device.</p>"""
    bgp_options: NotRequired[
        "capo_ec2.types.route_server_bgp_options.RouteServerBgpOptions"
    ]
    """<p>The BGP configuration options for this peer, including ASN (Autonomous System Number) and BFD (Bidrectional Forwarding Detection) settings.</p>"""
    bgp_status: NotRequired[
        "capo_ec2.types.route_server_bgp_status.RouteServerBgpStatus"
    ]
    """<p>The current status of the BGP session with this peer.</p>"""
    bfd_status: NotRequired[
        "capo_ec2.types.route_server_bfd_status.RouteServerBfdStatus"
    ]
    """<p>The current status of the BFD session with this peer.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the route server peer.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerPeer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_peer_id" in value:
        pairs.append(
            (f"{prefix}.RouteServerPeerId", str(value["route_server_peer_id"]))
        )
    if "route_server_endpoint_id" in value:
        pairs.append(
            (f"{prefix}.RouteServerEndpointId", str(value["route_server_endpoint_id"]))
        )
    if "route_server_id" in value:
        pairs.append((f"{prefix}.RouteServerId", str(value["route_server_id"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "state" in value:
        import capo_ec2.types.route_server_peer_state

        capo_ec2.types.route_server_peer_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "failure_reason" in value:
        pairs.append((f"{prefix}.FailureReason", str(value["failure_reason"])))
    if "endpoint_eni_id" in value:
        pairs.append((f"{prefix}.EndpointEniId", str(value["endpoint_eni_id"])))
    if "endpoint_eni_address" in value:
        pairs.append(
            (f"{prefix}.EndpointEniAddress", str(value["endpoint_eni_address"]))
        )
    if "peer_address" in value:
        pairs.append((f"{prefix}.PeerAddress", str(value["peer_address"])))
    if "bgp_options" in value:
        import capo_ec2.types.route_server_bgp_options

        capo_ec2.types.route_server_bgp_options.serialize_ec2_query(
            value["bgp_options"], pairs, f"{prefix}.BgpOptions"
        )
    if "bgp_status" in value:
        import capo_ec2.types.route_server_bgp_status

        capo_ec2.types.route_server_bgp_status.serialize_ec2_query(
            value["bgp_status"], pairs, f"{prefix}.BgpStatus"
        )
    if "bfd_status" in value:
        import capo_ec2.types.route_server_bfd_status

        capo_ec2.types.route_server_bfd_status.serialize_ec2_query(
            value["bfd_status"], pairs, f"{prefix}.BfdStatus"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> RouteServerPeer:
    out: RouteServerPeer = {}  # type: ignore[typeddict-item]
    child_route_server_peer_id = el.find("RouteServerPeerId")
    if child_route_server_peer_id is not None:
        out["route_server_peer_id"] = str(child_route_server_peer_id.text or "")
    child_route_server_endpoint_id = el.find("RouteServerEndpointId")
    if child_route_server_endpoint_id is not None:
        out["route_server_endpoint_id"] = str(child_route_server_endpoint_id.text or "")
    child_route_server_id = el.find("RouteServerId")
    if child_route_server_id is not None:
        out["route_server_id"] = str(child_route_server_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.route_server_peer_state

        out["state"] = capo_ec2.types.route_server_peer_state.deserialize_ec2_query(
            child_state
        )
    child_failure_reason = el.find("FailureReason")
    if child_failure_reason is not None:
        out["failure_reason"] = str(child_failure_reason.text or "")
    child_endpoint_eni_id = el.find("EndpointEniId")
    if child_endpoint_eni_id is not None:
        out["endpoint_eni_id"] = str(child_endpoint_eni_id.text or "")
    child_endpoint_eni_address = el.find("EndpointEniAddress")
    if child_endpoint_eni_address is not None:
        out["endpoint_eni_address"] = str(child_endpoint_eni_address.text or "")
    child_peer_address = el.find("PeerAddress")
    if child_peer_address is not None:
        out["peer_address"] = str(child_peer_address.text or "")
    child_bgp_options = el.find("BgpOptions")
    if child_bgp_options is not None:
        import capo_ec2.types.route_server_bgp_options

        out["bgp_options"] = (
            capo_ec2.types.route_server_bgp_options.deserialize_ec2_query(
                child_bgp_options
            )
        )
    child_bgp_status = el.find("BgpStatus")
    if child_bgp_status is not None:
        import capo_ec2.types.route_server_bgp_status

        out["bgp_status"] = (
            capo_ec2.types.route_server_bgp_status.deserialize_ec2_query(
                child_bgp_status
            )
        )
    child_bfd_status = el.find("BfdStatus")
    if child_bfd_status is not None:
        import capo_ec2.types.route_server_bfd_status

        out["bfd_status"] = (
            capo_ec2.types.route_server_bfd_status.deserialize_ec2_query(
                child_bfd_status
            )
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
