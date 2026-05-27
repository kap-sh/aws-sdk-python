"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_rule_id
    import aws_sdk_ec2.types.security_group_rule_request


class SecurityGroupRuleUpdate(TypedDict):
    security_group_rule_id: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_id.SecurityGroupRuleId"
    ]
    """<p>The ID of the security group rule.</p>"""
    security_group_rule: NotRequired[
        "aws_sdk_ec2.types.security_group_rule_request.SecurityGroupRuleRequest"
    ]
    """<p>Information about the security group rule.</p>"""
