"""Generated from Smithy shape ``com.amazonaws.ec2#RevokedSecurityGroupRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.revoked_security_group_rule

RevokedSecurityGroupRuleList: TypeAlias = list[
    "aws_sdk_ec2.types.revoked_security_group_rule.RevokedSecurityGroupRule"
]
