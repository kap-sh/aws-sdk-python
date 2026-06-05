"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectPeerList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_connect_peer

TransitGatewayConnectPeerList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_connect_peer.TransitGatewayConnectPeer"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConnectPeerList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.transit_gateway_connect_peer

        aws_sdk_ec2.types.transit_gateway_connect_peer.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> TransitGatewayConnectPeerList:
    import aws_sdk_ec2.types.transit_gateway_connect_peer

    out: TransitGatewayConnectPeerList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.transit_gateway_connect_peer.deserialize_ec2_query(child)
        )
    return out
