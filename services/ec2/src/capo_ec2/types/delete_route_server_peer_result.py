"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteRouteServerPeerResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_peer


class DeleteRouteServerPeerResult(TypedDict, closed=True):
    route_server_peer: NotRequired["capo_ec2.types.route_server_peer.RouteServerPeer"]
    """<p>Information about the deleted route server peer.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteRouteServerPeerResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server_peer" in value:
        import capo_ec2.types.route_server_peer

        capo_ec2.types.route_server_peer.serialize_ec2_query(
            value["route_server_peer"], pairs, f"{key_prefix}RouteServerPeer"
        )


def deserialize_ec2_query(el: Element) -> DeleteRouteServerPeerResult:
    out: DeleteRouteServerPeerResult = {}  # type: ignore[typeddict-item]
    child_route_server_peer = el.find("routeServerPeer")
    if child_route_server_peer is not None:
        import capo_ec2.types.route_server_peer

        out["route_server_peer"] = (
            capo_ec2.types.route_server_peer.deserialize_ec2_query(
                child_route_server_peer
            )
        )
    return out
