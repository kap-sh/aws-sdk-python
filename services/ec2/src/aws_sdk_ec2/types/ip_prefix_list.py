"""Generated from Smithy shape ``com.amazonaws.ec2#IpPrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string

IpPrefixList: TypeAlias = list["aws_sdk_ec2.types.string.String"]
