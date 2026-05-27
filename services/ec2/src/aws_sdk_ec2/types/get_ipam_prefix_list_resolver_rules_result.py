"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPrefixListResolverRulesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_set
    import aws_sdk_ec2.types.next_token


class GetIpamPrefixListResolverRulesResult(TypedDict):
    rules: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_set.IpamPrefixListResolverRuleSet"
    ]
    """<p>The CIDR selection rules for the IPAM prefix list resolver.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
