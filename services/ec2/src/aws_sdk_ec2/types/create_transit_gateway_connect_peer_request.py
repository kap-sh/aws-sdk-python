"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayConnectPeerRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
