"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayAttachmentBgpConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.bgp_status
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.string


class TransitGatewayAttachmentBgpConfiguration(TypedDict):
    transit_gateway_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The transit gateway Autonomous System Number (ASN).</p>"""
    peer_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The peer Autonomous System Number (ASN).</p>"""
    transit_gateway_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The interior BGP peer IP address for the transit gateway.</p>"""
    peer_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The interior BGP peer IP address for the appliance.</p>"""
    bgp_status: NotRequired["aws_sdk_ec2.types.bgp_status.BgpStatus"]
    """<p>The BGP status.</p>"""
