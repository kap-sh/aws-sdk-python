"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_rule_update

SecurityGroupRuleUpdateList: TypeAlias = list[
    "aws_sdk_ec2.types.security_group_rule_update.SecurityGroupRuleUpdate"
]
