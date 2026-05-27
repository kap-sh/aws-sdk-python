"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleConditionSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition

IpamPrefixListResolverRuleConditionSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition.IpamPrefixListResolverRuleCondition"
]
