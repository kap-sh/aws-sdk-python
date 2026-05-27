"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreManagedPrefixListVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.prefix_list_resource_id


class RestoreManagedPrefixListVersionRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    previous_version: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The version to restore.</p>"""
    current_version: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The current version number for the prefix list.</p>"""
