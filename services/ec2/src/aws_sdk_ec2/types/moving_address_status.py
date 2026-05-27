"""Generated from Smithy shape ``com.amazonaws.ec2#MovingAddressStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.move_status
    import aws_sdk_ec2.types.string


class MovingAddressStatus(TypedDict):
    move_status: NotRequired["aws_sdk_ec2.types.move_status.MoveStatus"]
    """<p>The status of the Elastic IP address that's being moved or restored.</p>"""
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Elastic IP address.</p>"""
