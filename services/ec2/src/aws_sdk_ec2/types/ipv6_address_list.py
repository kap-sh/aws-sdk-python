"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string

Ipv6AddressList: TypeAlias = list["aws_sdk_ec2.types.string.String"]
