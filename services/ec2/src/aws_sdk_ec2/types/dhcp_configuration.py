"""Generated from Smithy shape ``com.amazonaws.ec2#DhcpConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dhcp_configuration_value_list
    import aws_sdk_ec2.types.string


class DhcpConfiguration(TypedDict):
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of a DHCP option.</p>"""
    values: NotRequired[
        "aws_sdk_ec2.types.dhcp_configuration_value_list.DhcpConfigurationValueList"
    ]
    """<p>The values for the DHCP option.</p>"""
