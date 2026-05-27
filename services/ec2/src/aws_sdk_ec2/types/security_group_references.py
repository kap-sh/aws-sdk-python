"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_reference

SecurityGroupReferences: TypeAlias = list[
    "aws_sdk_ec2.types.security_group_reference.SecurityGroupReference"
]
