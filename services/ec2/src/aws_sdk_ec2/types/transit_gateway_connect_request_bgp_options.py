"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectRequestBgpOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.long


class TransitGatewayConnectRequestBgpOptions(TypedDict):
    peer_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The peer Autonomous System Number (ASN).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConnectRequestBgpOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "peer_asn" in value:
        pairs.append((f"{prefix}.PeerAsn", str(value["peer_asn"])))


def deserialize_ec2_query(el: Element) -> TransitGatewayConnectRequestBgpOptions:
    out: TransitGatewayConnectRequestBgpOptions = {}  # type: ignore[typeddict-item]
    child_peer_asn = el.find("PeerAsn")
    if child_peer_asn is not None:
        out["peer_asn"] = int(child_peer_asn.text or "")
    return out
