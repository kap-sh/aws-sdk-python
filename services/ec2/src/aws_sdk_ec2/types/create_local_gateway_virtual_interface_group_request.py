"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayVirtualInterfaceGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.local_gateway_id
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.tag_specification_list


class CreateLocalGatewayVirtualInterfaceGroupRequest(TypedDict):
    local_gateway_id: NotRequired["aws_sdk_ec2.types.local_gateway_id.LocalGatewayId"]
    """<p>The ID of the local gateway.</p>"""
    local_bgp_asn: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Autonomous System Number(ASN) for the local Border Gateway Protocol (BGP).</p>"""
    local_bgp_asn_extended: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The extended 32-bit ASN for the local BGP configuration.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the local gateway virtual interface group when the resource is being created.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
