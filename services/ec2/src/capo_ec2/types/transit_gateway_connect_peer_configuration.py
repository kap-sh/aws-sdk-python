"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectPeerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.inside_cidr_blocks_string_list
    import capo_ec2.types.protocol_value
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_attachment_bgp_configuration_list


class TransitGatewayConnectPeerConfiguration(TypedDict, closed=True):
    transit_gateway_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The Connect peer IP address on the transit gateway side of the tunnel.</p>"""
    peer_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The Connect peer IP address on the appliance side of the tunnel.</p>"""
    inside_cidr_blocks: NotRequired[
        "capo_ec2.types.inside_cidr_blocks_string_list.InsideCidrBlocksStringList"
    ]
    """<p>The range of interior BGP peer IP addresses.</p>"""
    protocol: NotRequired["capo_ec2.types.protocol_value.ProtocolValue"]
    """<p>The tunnel protocol.</p>"""
    bgp_configurations: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_bgp_configuration_list.TransitGatewayAttachmentBgpConfigurationList"
    ]
    """<p>The BGP configuration details.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConnectPeerConfiguration,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_address" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAddress",
                str(value["transit_gateway_address"]),
            )
        )
    if "peer_address" in value:
        pairs.append((f"{key_prefix}PeerAddress", str(value["peer_address"])))
    if "inside_cidr_blocks" in value:
        import capo_ec2.types.inside_cidr_blocks_string_list

        capo_ec2.types.inside_cidr_blocks_string_list.serialize_ec2_query(
            value["inside_cidr_blocks"], pairs, f"{key_prefix}InsideCidrBlocks"
        )
    if "protocol" in value:
        import capo_ec2.types.protocol_value

        capo_ec2.types.protocol_value.serialize_ec2_query(
            value["protocol"], pairs, f"{key_prefix}Protocol"
        )
    if "bgp_configurations" in value:
        import capo_ec2.types.transit_gateway_attachment_bgp_configuration_list

        capo_ec2.types.transit_gateway_attachment_bgp_configuration_list.serialize_ec2_query(
            value["bgp_configurations"], pairs, f"{key_prefix}BgpConfigurations"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayConnectPeerConfiguration:
    out: TransitGatewayConnectPeerConfiguration = {}  # type: ignore[typeddict-item]
    child_transit_gateway_address = el.find("transitGatewayAddress")
    if child_transit_gateway_address is not None:
        out["transit_gateway_address"] = str(child_transit_gateway_address.text or "")
    child_peer_address = el.find("peerAddress")
    if child_peer_address is not None:
        out["peer_address"] = str(child_peer_address.text or "")
    if el.find("insideCidrBlocks") is not None:
        import capo_ec2.types.inside_cidr_blocks_string_list

        out["inside_cidr_blocks"] = (
            capo_ec2.types.inside_cidr_blocks_string_list.deserialize_ec2_query(
                el, "insideCidrBlocks"
            )
        )
    child_protocol = el.find("protocol")
    if child_protocol is not None:
        import capo_ec2.types.protocol_value

        out["protocol"] = capo_ec2.types.protocol_value.deserialize_ec2_query(
            child_protocol
        )
    if el.find("bgpConfigurations") is not None:
        import capo_ec2.types.transit_gateway_attachment_bgp_configuration_list

        out["bgp_configurations"] = (
            capo_ec2.types.transit_gateway_attachment_bgp_configuration_list.deserialize_ec2_query(
                el, "bgpConfigurations"
            )
        )
    return out
