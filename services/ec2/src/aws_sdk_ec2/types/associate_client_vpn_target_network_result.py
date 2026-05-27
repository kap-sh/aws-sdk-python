"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateClientVpnTargetNetworkResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.association_status
    import aws_sdk_ec2.types.string


class AssociateClientVpnTargetNetworkResult(TypedDict):
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The unique ID of the target network association.</p>"""
    status: NotRequired["aws_sdk_ec2.types.association_status.AssociationStatus"]
    """<p>The current state of the target network association.</p>"""
