"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectPeerConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.inside_cidr_blocks_string_list
    import aws_sdk_ec2.types.protocol_value
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration_list


class TransitGatewayConnectPeerConfiguration(TypedDict):
    transit_gateway_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Connect peer IP address on the transit gateway side of the tunnel.</p>"""
    peer_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Connect peer IP address on the appliance side of the tunnel.</p>"""
    inside_cidr_blocks: NotRequired[
        "aws_sdk_ec2.types.inside_cidr_blocks_string_list.InsideCidrBlocksStringList"
    ]
    """<p>The range of interior BGP peer IP addresses.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.protocol_value.ProtocolValue"]
    """<p>The tunnel protocol.</p>"""
    bgp_configurations: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration_list.TransitGatewayAttachmentBgpConfigurationList"
    ]
    """<p>The BGP configuration details.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConnectPeerConfiguration,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_address" in value:
        pairs.append(
            (f"{prefix}.TransitGatewayAddress", str(value["transit_gateway_address"]))
        )
    if "peer_address" in value:
        pairs.append((f"{prefix}.PeerAddress", str(value["peer_address"])))
    if "inside_cidr_blocks" in value:
        import aws_sdk_ec2.types.inside_cidr_blocks_string_list

        aws_sdk_ec2.types.inside_cidr_blocks_string_list.serialize_ec2_query(
            value["inside_cidr_blocks"], pairs, f"{prefix}.InsideCidrBlocks"
        )
    if "protocol" in value:
        import aws_sdk_ec2.types.protocol_value

        aws_sdk_ec2.types.protocol_value.serialize_ec2_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )
    if "bgp_configurations" in value:
        import aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration_list

        aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration_list.serialize_ec2_query(
            value["bgp_configurations"], pairs, f"{prefix}.BgpConfigurations"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayConnectPeerConfiguration:
    out: TransitGatewayConnectPeerConfiguration = {}  # type: ignore[typeddict-item]
    child_transit_gateway_address = el.find("TransitGatewayAddress")
    if child_transit_gateway_address is not None:
        out["transit_gateway_address"] = str(child_transit_gateway_address.text or "")
    child_peer_address = el.find("PeerAddress")
    if child_peer_address is not None:
        out["peer_address"] = str(child_peer_address.text or "")
    if el.find("InsideCidrBlocks") is not None:
        import aws_sdk_ec2.types.inside_cidr_blocks_string_list

        out["inside_cidr_blocks"] = (
            aws_sdk_ec2.types.inside_cidr_blocks_string_list.deserialize_ec2_query(
                el, "InsideCidrBlocks"
            )
        )
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import aws_sdk_ec2.types.protocol_value

        out["protocol"] = aws_sdk_ec2.types.protocol_value.deserialize_ec2_query(
            child_protocol
        )
    if el.find("BgpConfigurations") is not None:
        import aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration_list

        out["bgp_configurations"] = (
            aws_sdk_ec2.types.transit_gateway_attachment_bgp_configuration_list.deserialize_ec2_query(
                el, "BgpConfigurations"
            )
        )
    return out
