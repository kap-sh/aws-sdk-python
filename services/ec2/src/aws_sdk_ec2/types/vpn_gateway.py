"""Generated from Smithy shape ``com.amazonaws.ec2#VpnGateway``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.gateway_type
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_attachment_list
    import aws_sdk_ec2.types.vpn_state


class VpnGateway(TypedDict):
    amazon_side_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The private Autonomous System Number (ASN) for the Amazon side of a BGP session.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the virtual private gateway.</p>"""
    vpn_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the virtual private gateway.</p>"""
    state: NotRequired["aws_sdk_ec2.types.vpn_state.VpnState"]
    """<p>The current state of the virtual private gateway.</p>"""
    type: NotRequired["aws_sdk_ec2.types.gateway_type.GatewayType"]
    """<p>The type of VPN connection the virtual private gateway supports.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone where the virtual private gateway was created, if applicable. This field may be empty or not returned.</p>"""
    vpc_attachments: NotRequired[
        "aws_sdk_ec2.types.vpc_attachment_list.VpcAttachmentList"
    ]
    """<p>Any VPCs attached to the virtual private gateway.</p>"""
