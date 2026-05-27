"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectPeerConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
