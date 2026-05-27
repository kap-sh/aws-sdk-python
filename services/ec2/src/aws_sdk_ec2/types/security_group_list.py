"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group

SecurityGroupList: TypeAlias = list["aws_sdk_ec2.types.security_group.SecurityGroup"]
