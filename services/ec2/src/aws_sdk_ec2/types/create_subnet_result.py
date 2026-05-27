"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSubnetResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet


class CreateSubnetResult(TypedDict):
    subnet: NotRequired["aws_sdk_ec2.types.subnet.Subnet"]
    """<p>Information about the subnet.</p>"""
