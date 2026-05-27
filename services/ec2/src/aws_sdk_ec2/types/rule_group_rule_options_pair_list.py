"""Generated from Smithy shape ``com.amazonaws.ec2#RuleGroupRuleOptionsPairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.rule_group_rule_options_pair

RuleGroupRuleOptionsPairList: TypeAlias = list[
    "aws_sdk_ec2.types.rule_group_rule_options_pair.RuleGroupRuleOptionsPair"
]
