"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPrefixListResolversResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_set
    import aws_sdk_ec2.types.next_token


class DescribeIpamPrefixListResolversResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_prefix_list_resolvers: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_set.IpamPrefixListResolverSet"
    ]
    """<p>Information about the IPAM prefix list resolvers.</p>"""
