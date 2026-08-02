"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayConnectPeerResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_connect_peer


class CreateTransitGatewayConnectPeerResult(TypedDict, closed=True):
    transit_gateway_connect_peer: NotRequired[
        "capo_ec2.types.transit_gateway_connect_peer.TransitGatewayConnectPeer"
    ]
    """<p>Information about the Connect peer.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayConnectPeerResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_connect_peer" in value:
        import capo_ec2.types.transit_gateway_connect_peer

        capo_ec2.types.transit_gateway_connect_peer.serialize_ec2_query(
            value["transit_gateway_connect_peer"],
            pairs,
            f"{key_prefix}TransitGatewayConnectPeer",
        )


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayConnectPeerResult:
    out: CreateTransitGatewayConnectPeerResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_connect_peer = el.find("TransitGatewayConnectPeer")
    if child_transit_gateway_connect_peer is not None:
        import capo_ec2.types.transit_gateway_connect_peer

        out["transit_gateway_connect_peer"] = (
            capo_ec2.types.transit_gateway_connect_peer.deserialize_ec2_query(
                child_transit_gateway_connect_peer
            )
        )
    return out
