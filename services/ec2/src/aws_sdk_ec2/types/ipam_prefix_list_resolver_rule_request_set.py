"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleRequestSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_request

IpamPrefixListResolverRuleRequestSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_request.IpamPrefixListResolverRuleRequest"
]
