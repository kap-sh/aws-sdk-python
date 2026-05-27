"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_rule_description

SecurityGroupRuleDescriptionList: TypeAlias = list[
    "aws_sdk_ec2.types.security_group_rule_description.SecurityGroupRuleDescription"
]
