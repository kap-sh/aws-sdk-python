"""Generated from Smithy shape ``com.amazonaws.ec2#DhcpOptionsIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dhcp_options_id

DhcpOptionsIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.dhcp_options_id.DhcpOptionsId"
]
