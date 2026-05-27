"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeManagedPrefixListsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.managed_prefix_list_set
    import aws_sdk_ec2.types.next_token


class DescribeManagedPrefixListsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    prefix_lists: NotRequired[
        "aws_sdk_ec2.types.managed_prefix_list_set.ManagedPrefixListSet"
    ]
    """<p>Information about the prefix lists.</p>"""
