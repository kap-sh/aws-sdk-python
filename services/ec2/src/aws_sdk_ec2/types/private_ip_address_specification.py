"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateIpAddressSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class PrivateIpAddressSpecification(TypedDict):
    primary: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.</p>"""
    private_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private IPv4 address.</p>"""
