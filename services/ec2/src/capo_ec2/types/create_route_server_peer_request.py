"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRouteServerPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.route_server_bgp_options_request
    import capo_ec2.types.route_server_endpoint_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateRouteServerPeerRequest(TypedDict, closed=True):
    route_server_endpoint_id: NotRequired[
        "capo_ec2.types.route_server_endpoint_id.RouteServerEndpointId"
    ]
    """<p>The ID of the route server endpoint for which to create a peer.</p>"""
    peer_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address of the peer device.</p>"""
    bgp_options: NotRequired[
        "capo_ec2.types.route_server_bgp_options_request.RouteServerBgpOptionsRequest"
    ]
    """<p>The BGP options for the peer, including ASN (Autonomous System Number) and BFD (Bidrectional Forwarding Detection) settings.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the route server peer during creation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateRouteServerPeerRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server_endpoint_id" in value:
        pairs.append(
            (
                f"{key_prefix}RouteServerEndpointId",
                str(value["route_server_endpoint_id"]),
            )
        )
    if "peer_address" in value:
        pairs.append((f"{key_prefix}PeerAddress", str(value["peer_address"])))
    if "bgp_options" in value:
        import capo_ec2.types.route_server_bgp_options_request

        capo_ec2.types.route_server_bgp_options_request.serialize_ec2_query(
            value["bgp_options"], pairs, f"{key_prefix}BgpOptions"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )


def deserialize_ec2_query(el: Element) -> CreateRouteServerPeerRequest:
    out: CreateRouteServerPeerRequest = {}  # type: ignore[typeddict-item]
    child_route_server_endpoint_id = el.find("RouteServerEndpointId")
    if child_route_server_endpoint_id is not None:
        out["route_server_endpoint_id"] = str(child_route_server_endpoint_id.text or "")
    child_peer_address = el.find("PeerAddress")
    if child_peer_address is not None:
        out["peer_address"] = str(child_peer_address.text or "")
    child_bgp_options = el.find("BgpOptions")
    if child_bgp_options is not None:
        import capo_ec2.types.route_server_bgp_options_request

        out["bgp_options"] = (
            capo_ec2.types.route_server_bgp_options_request.deserialize_ec2_query(
                child_bgp_options
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    return out
