"""Generated from Smithy shape ``com.amazonaws.ec2#RuleGroupTypePair``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string


class RuleGroupTypePair(TypedDict):
    rule_group_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the rule group.</p>"""
    rule_group_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The rule group type. The possible values are <code>Domain List</code> and <code>Suricata</code>.</p>"""
