"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePrefixListsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.prefix_list_set
    import aws_sdk_ec2.types.string


class DescribePrefixListsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    prefix_lists: NotRequired["aws_sdk_ec2.types.prefix_list_set.PrefixListSet"]
    """<p>All available prefix lists.</p>"""
