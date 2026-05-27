"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPrefixListResolverTargetsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_target_set
    import aws_sdk_ec2.types.next_token


class DescribeIpamPrefixListResolverTargetsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_prefix_list_resolver_targets: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_target_set.IpamPrefixListResolverTargetSet"
    ]
    """<p>Information about the IPAM prefix list resolver Targets.</p>"""
