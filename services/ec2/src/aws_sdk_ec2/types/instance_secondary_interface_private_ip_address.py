"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfacePrivateIpAddress``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class InstanceSecondaryInterfacePrivateIpAddress(TypedDict):
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private IPv4 address.</p>"""
