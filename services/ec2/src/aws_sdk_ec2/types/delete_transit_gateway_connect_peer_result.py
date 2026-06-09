"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayConnectPeerResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_connect_peer


class DeleteTransitGatewayConnectPeerResult(TypedDict):
    transit_gateway_connect_peer: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_peer.TransitGatewayConnectPeer"
    ]
    """<p>Information about the deleted Connect peer.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayConnectPeerResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_connect_peer" in value:
        import aws_sdk_ec2.types.transit_gateway_connect_peer

        aws_sdk_ec2.types.transit_gateway_connect_peer.serialize_ec2_query(
            value["transit_gateway_connect_peer"],
            pairs,
            f"{prefix}.TransitGatewayConnectPeer",
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayConnectPeerResult:
    out: DeleteTransitGatewayConnectPeerResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_connect_peer = el.find("TransitGatewayConnectPeer")
    if child_transit_gateway_connect_peer is not None:
        import aws_sdk_ec2.types.transit_gateway_connect_peer

        out["transit_gateway_connect_peer"] = (
            aws_sdk_ec2.types.transit_gateway_connect_peer.deserialize_ec2_query(
                child_transit_gateway_connect_peer
            )
        )
    return out
