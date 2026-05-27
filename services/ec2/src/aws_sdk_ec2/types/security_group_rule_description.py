"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupRuleDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class SecurityGroupRuleDescription(TypedDict):
    security_group_rule_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the security group rule.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the security group rule.</p>"""
