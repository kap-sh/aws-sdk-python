"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDhcpOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dhcp_options


class CreateDhcpOptionsResult(TypedDict):
    dhcp_options: NotRequired["aws_sdk_ec2.types.dhcp_options.DhcpOptions"]
    """<p>A set of DHCP options.</p>"""
