"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayConnectPeerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.inside_cidr_blocks_string_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_connect_request_bgp_options


class CreateTransitGatewayConnectPeerRequest(TypedDict):
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the Connect attachment.</p>"""
    transit_gateway_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The peer IP address (GRE outer IP address) on the transit gateway side of the Connect peer, which must be specified from a transit gateway CIDR block. If not specified, Amazon automatically assigns the first available IP address from the transit gateway CIDR block.</p>"""
    peer_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The peer IP address (GRE outer IP address) on the appliance side of the Connect peer.</p>"""
    bgp_options: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_request_bgp_options.TransitGatewayConnectRequestBgpOptions"
    ]
    """<p>The BGP options for the Connect peer.</p>"""
    inside_cidr_blocks: NotRequired[
        "aws_sdk_ec2.types.inside_cidr_blocks_string_list.InsideCidrBlocksStringList"
    ]
    """<p>The range of inside IP addresses that are used for BGP peering. You must specify a size /29 IPv4 CIDR block from the <code>169.254.0.0/16</code> range. The first address from the range must be configured on the appliance as the BGP IP address. You can also optionally specify a size /125 IPv6 CIDR block from the <code>fd00::/8</code> range.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the Connect peer.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayConnectPeerRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{prefix}.TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "transit_gateway_address" in value:
        pairs.append(
            (f"{prefix}.TransitGatewayAddress", str(value["transit_gateway_address"]))
        )
    if "peer_address" in value:
        pairs.append((f"{prefix}.PeerAddress", str(value["peer_address"])))
    if "bgp_options" in value:
        import aws_sdk_ec2.types.transit_gateway_connect_request_bgp_options

        aws_sdk_ec2.types.transit_gateway_connect_request_bgp_options.serialize_ec2_query(
            value["bgp_options"], pairs, f"{prefix}.BgpOptions"
        )
    if "inside_cidr_blocks" in value:
        import aws_sdk_ec2.types.inside_cidr_blocks_string_list

        aws_sdk_ec2.types.inside_cidr_blocks_string_list.serialize_ec2_query(
            value["inside_cidr_blocks"], pairs, f"{prefix}.InsideCidrBlocks"
        )
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayConnectPeerRequest:
    out: CreateTransitGatewayConnectPeerRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_transit_gateway_address = el.find("TransitGatewayAddress")
    if child_transit_gateway_address is not None:
        out["transit_gateway_address"] = str(child_transit_gateway_address.text or "")
    child_peer_address = el.find("PeerAddress")
    if child_peer_address is not None:
        out["peer_address"] = str(child_peer_address.text or "")
    child_bgp_options = el.find("BgpOptions")
    if child_bgp_options is not None:
        import aws_sdk_ec2.types.transit_gateway_connect_request_bgp_options

        out["bgp_options"] = (
            aws_sdk_ec2.types.transit_gateway_connect_request_bgp_options.deserialize_ec2_query(
                child_bgp_options
            )
        )
    if el.find("InsideCidrBlocks") is not None:
        import aws_sdk_ec2.types.inside_cidr_blocks_string_list

        out["inside_cidr_blocks"] = (
            aws_sdk_ec2.types.inside_cidr_blocks_string_list.deserialize_ec2_query(
                el, "InsideCidrBlocks"
            )
        )
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
