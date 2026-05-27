"""Generated from Smithy shape ``com.amazonaws.ec2#GetManagedPrefixListEntriesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.prefix_list_entry_set


class GetManagedPrefixListEntriesResult(TypedDict):
    entries: NotRequired["aws_sdk_ec2.types.prefix_list_entry_set.PrefixListEntrySet"]
    """<p>Information about the prefix list entries.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
