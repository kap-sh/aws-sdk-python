"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConcentrator``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class VpnConcentrator(TypedDict):
    vpn_concentrator_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPN concentrator.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of the VPN concentrator.</p>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway associated with the VPN concentrator.</p>"""
    transit_gateway_attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway attachment for the VPN concentrator.</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of VPN concentrator.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the VPN concentrator.</p>"""
