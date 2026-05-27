"""Generated from Smithy shape ``com.amazonaws.ec2#TargetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.target_group

TargetGroups: TypeAlias = list["aws_sdk_ec2.types.target_group.TargetGroup"]
