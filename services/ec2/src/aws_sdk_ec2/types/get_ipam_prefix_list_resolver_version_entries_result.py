"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPrefixListResolverVersionEntriesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_version_entry_set
    import aws_sdk_ec2.types.next_token


class GetIpamPrefixListResolverVersionEntriesResult(TypedDict):
    entries: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_version_entry_set.IpamPrefixListResolverVersionEntrySet"
    ]
    """<p>The CIDR entries for the specified resolver version.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
