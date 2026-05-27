"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizeSecurityGroupEgressResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.security_group_rule_list

AuthorizeSecurityGroupEgressResult = TypedDict(
    "AuthorizeSecurityGroupEgressResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
        "security_group_rules": NotRequired[
            "aws_sdk_ec2.types.security_group_rule_list.SecurityGroupRuleList"
        ],
    },
)
