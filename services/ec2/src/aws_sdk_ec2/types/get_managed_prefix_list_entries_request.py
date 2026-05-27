"""Generated from Smithy shape ``com.amazonaws.ec2#GetManagedPrefixListEntriesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.prefix_list_max_results
    import aws_sdk_ec2.types.prefix_list_resource_id


class GetManagedPrefixListEntriesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    target_version: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The version of the prefix list for which to return the entries. The default is the current version.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.prefix_list_max_results.PrefixListMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
