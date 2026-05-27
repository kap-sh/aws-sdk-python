"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDefaultSubnetResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet


class CreateDefaultSubnetResult(TypedDict):
    subnet: NotRequired["aws_sdk_ec2.types.subnet.Subnet"]
    """<p>Information about the subnet.</p>"""
