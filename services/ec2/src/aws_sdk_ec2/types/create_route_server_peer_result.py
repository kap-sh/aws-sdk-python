"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRouteServerPeerResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_peer


class CreateRouteServerPeerResult(TypedDict):
    route_server_peer: NotRequired[
        "aws_sdk_ec2.types.route_server_peer.RouteServerPeer"
    ]
    """<p>Information about the created route server peer.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateRouteServerPeerResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_peer" in value:
        import aws_sdk_ec2.types.route_server_peer

        aws_sdk_ec2.types.route_server_peer.serialize_ec2_query(
            value["route_server_peer"], pairs, f"{prefix}.RouteServerPeer"
        )


def deserialize_ec2_query(el: Element) -> CreateRouteServerPeerResult:
    out: CreateRouteServerPeerResult = {}  # type: ignore[typeddict-item]
    child_route_server_peer = el.find("RouteServerPeer")
    if child_route_server_peer is not None:
        import aws_sdk_ec2.types.route_server_peer

        out["route_server_peer"] = (
            aws_sdk_ec2.types.route_server_peer.deserialize_ec2_query(
                child_route_server_peer
            )
        )
    return out
