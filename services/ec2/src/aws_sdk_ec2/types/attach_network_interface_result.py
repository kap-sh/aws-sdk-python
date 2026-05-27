"""Generated from Smithy shape ``com.amazonaws.ec2#AttachNetworkInterfaceResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class AttachNetworkInterfaceResult(TypedDict):
    attachment_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface attachment.</p>"""
    network_card_index: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The index of the network card.</p>"""
