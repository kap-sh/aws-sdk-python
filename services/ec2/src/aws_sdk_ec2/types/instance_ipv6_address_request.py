"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv6AddressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class InstanceIpv6AddressRequest(TypedDict):
    ipv6_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 address.</p>"""
