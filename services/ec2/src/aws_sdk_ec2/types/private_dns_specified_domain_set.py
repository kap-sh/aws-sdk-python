"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsSpecifiedDomainSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string

PrivateDnsSpecifiedDomainSet: TypeAlias = list["aws_sdk_ec2.types.string.String"]
