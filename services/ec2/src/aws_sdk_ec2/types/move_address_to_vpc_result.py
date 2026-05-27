"""Generated from Smithy shape ``com.amazonaws.ec2#MoveAddressToVpcResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.status
    import aws_sdk_ec2.types.string


class MoveAddressToVpcResult(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The allocation ID for the Elastic IP address.</p>"""
    status: NotRequired["aws_sdk_ec2.types.status.Status"]
    """<p>The status of the move of the IP address.</p>"""
