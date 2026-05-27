"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_id
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.outpost_lag_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateLocalGatewayVirtualInterfaceRequest(TypedDict):
    local_gateway_virtual_interface_group_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group_id.LocalGatewayVirtualInterfaceGroupId"
    ]
    """<p>The ID of the local gateway virtual interface group.</p>"""
    outpost_lag_id: NotRequired["aws_sdk_ec2.types.outpost_lag_id.OutpostLagId"]
    """<p>References the Link Aggregation Group (LAG) that connects the Outpost to on-premises network devices.</p>"""
    vlan: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The virtual local area network (VLAN) used for the local gateway virtual interface.</p>"""
    local_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address assigned to the local gateway virtual interface on the Outpost side. Only IPv4 is supported.</p>"""
    peer_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The peer IP address for the local gateway virtual interface. Only IPv4 is supported.</p>"""
    peer_bgp_asn: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Autonomous System Number (ASN) of the Border Gateway Protocol (BGP) peer.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to a resource when the local gateway virtual interface is being created. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    peer_bgp_asn_extended: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The extended 32-bit ASN of the BGP peer for use with larger ASN values.</p>"""
