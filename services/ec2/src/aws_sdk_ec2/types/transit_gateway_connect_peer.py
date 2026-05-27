"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectPeer``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.transit_gateway_connect_peer_configuration
    import aws_sdk_ec2.types.transit_gateway_connect_peer_id
    import aws_sdk_ec2.types.transit_gateway_connect_peer_state


class TransitGatewayConnectPeer(TypedDict):
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the Connect attachment.</p>"""
    transit_gateway_connect_peer_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_peer_id.TransitGatewayConnectPeerId"
    ]
    """<p>The ID of the Connect peer.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_peer_state.TransitGatewayConnectPeerState"
    ]
    """<p>The state of the Connect peer.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The creation time.</p>"""
    connect_peer_configuration: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_peer_configuration.TransitGatewayConnectPeerConfiguration"
    ]
    """<p>The Connect peer details.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the Connect peer.</p>"""
