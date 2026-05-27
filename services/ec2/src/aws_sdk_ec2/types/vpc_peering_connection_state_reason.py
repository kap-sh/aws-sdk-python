"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnectionStateReason``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_peering_connection_state_reason_code


class VpcPeeringConnectionStateReason(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_state_reason_code.VpcPeeringConnectionStateReasonCode"
    ]
    """<p>The status of the VPC peering connection.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message that provides more information about the status, if applicable.</p>"""
