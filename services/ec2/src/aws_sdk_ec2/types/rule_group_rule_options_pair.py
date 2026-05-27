"""Generated from Smithy shape ``com.amazonaws.ec2#RuleGroupRuleOptionsPair``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.rule_option_list


class RuleGroupRuleOptionsPair(TypedDict):
    rule_group_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the rule group.</p>"""
    rule_options: NotRequired["aws_sdk_ec2.types.rule_option_list.RuleOptionList"]
    """<p>The rule options.</p>"""
