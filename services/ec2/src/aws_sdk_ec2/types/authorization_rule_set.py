"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizationRuleSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.authorization_rule

AuthorizationRuleSet: TypeAlias = list[
    "aws_sdk_ec2.types.authorization_rule.AuthorizationRule"
]
