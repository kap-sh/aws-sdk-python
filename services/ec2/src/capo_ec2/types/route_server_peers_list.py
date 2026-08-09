"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPeersList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_peer

RouteServerPeersList: TypeAlias = list[
    "capo_ec2.types.route_server_peer.RouteServerPeer"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerPeersList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.route_server_peer

        capo_ec2.types.route_server_peer.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> RouteServerPeersList:
    import capo_ec2.types.route_server_peer

    out: RouteServerPeersList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.route_server_peer.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> RouteServerPeersList:
    import capo_ec2.types.route_server_peer

    out: RouteServerPeersList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.route_server_peer.deserialize_ec2_query(child))
    return out
