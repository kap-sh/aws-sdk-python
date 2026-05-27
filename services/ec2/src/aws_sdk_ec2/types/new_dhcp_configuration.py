"""Generated from Smithy shape ``com.amazonaws.ec2#NewDhcpConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class NewDhcpConfiguration(TypedDict):
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of a DHCP option.</p>"""
    values: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The values for the DHCP option.</p>"""
