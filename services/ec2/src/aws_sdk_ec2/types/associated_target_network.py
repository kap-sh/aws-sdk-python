"""Generated from Smithy shape ``com.amazonaws.ec2#AssociatedTargetNetwork``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associated_network_type
    import aws_sdk_ec2.types.string


class AssociatedTargetNetwork(TypedDict):
    network_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    network_type: NotRequired[
        "aws_sdk_ec2.types.associated_network_type.AssociatedNetworkType"
    ]
    """<p>The target network type.</p>"""
