"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentBgpConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.bgp_status
    import capo_ec2.types.long
    import capo_ec2.types.string


class TransitGatewayAttachmentBgpConfiguration(TypedDict, closed=True):
    transit_gateway_asn: NotRequired["capo_ec2.types.long.Long"]
    """<p>The transit gateway Autonomous System Number (ASN).</p>"""
    peer_asn: NotRequired["capo_ec2.types.long.Long"]
    """<p>The peer Autonomous System Number (ASN).</p>"""
    transit_gateway_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The interior BGP peer IP address for the transit gateway.</p>"""
    peer_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The interior BGP peer IP address for the appliance.</p>"""
    bgp_status: NotRequired["capo_ec2.types.bgp_status.BgpStatus"]
    """<p>The BGP status.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayAttachmentBgpConfiguration,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_asn" in value:
        pairs.append((f"{prefix}.TransitGatewayAsn", str(value["transit_gateway_asn"])))
    if "peer_asn" in value:
        pairs.append((f"{prefix}.PeerAsn", str(value["peer_asn"])))
    if "transit_gateway_address" in value:
        pairs.append(
            (f"{prefix}.TransitGatewayAddress", str(value["transit_gateway_address"]))
        )
    if "peer_address" in value:
        pairs.append((f"{prefix}.PeerAddress", str(value["peer_address"])))
    if "bgp_status" in value:
        import capo_ec2.types.bgp_status

        capo_ec2.types.bgp_status.serialize_ec2_query(
            value["bgp_status"], pairs, f"{prefix}.BgpStatus"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayAttachmentBgpConfiguration:
    out: TransitGatewayAttachmentBgpConfiguration = {}  # type: ignore[typeddict-item]
    child_transit_gateway_asn = el.find("TransitGatewayAsn")
    if child_transit_gateway_asn is not None:
        out["transit_gateway_asn"] = int(child_transit_gateway_asn.text or "")
    child_peer_asn = el.find("PeerAsn")
    if child_peer_asn is not None:
        out["peer_asn"] = int(child_peer_asn.text or "")
    child_transit_gateway_address = el.find("TransitGatewayAddress")
    if child_transit_gateway_address is not None:
        out["transit_gateway_address"] = str(child_transit_gateway_address.text or "")
    child_peer_address = el.find("PeerAddress")
    if child_peer_address is not None:
        out["peer_address"] = str(child_peer_address.text or "")
    child_bgp_status = el.find("BgpStatus")
    if child_bgp_status is not None:
        import capo_ec2.types.bgp_status

        out["bgp_status"] = capo_ec2.types.bgp_status.deserialize_ec2_query(
            child_bgp_status
        )
    return out
