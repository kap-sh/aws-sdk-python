"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyManagedPrefixListRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.add_prefix_list_entries
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.remove_prefix_list_entries
    import aws_sdk_ec2.types.string


class ModifyManagedPrefixListRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    current_version: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The current version of the prefix list.</p>"""
    prefix_list_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A name for the prefix list.</p>"""
    add_entries: NotRequired[
        "aws_sdk_ec2.types.add_prefix_list_entries.AddPrefixListEntries"
    ]
    """<p>One or more entries to add to the prefix list.</p>"""
    remove_entries: NotRequired[
        "aws_sdk_ec2.types.remove_prefix_list_entries.RemovePrefixListEntries"
    ]
    """<p>One or more entries to remove from the prefix list.</p>"""
    max_entries: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of entries for the prefix list. You cannot modify the entries of a prefix list and modify the size of a prefix list at the same time.</p> <p>If any of the resources that reference the prefix list cannot support the new maximum size, the modify operation fails. Check the state message for the IDs of the first ten resources that do not support the new maximum size.</p>"""
    ipam_prefix_list_resolver_sync_enabled: NotRequired[
        "aws_sdk_ec2.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Indicates whether synchronization with an IPAM prefix list resolver should be enabled for this managed prefix list. When enabled, the prefix list CIDRs are automatically updated based on the associated resolver's CIDR selection rules.</p>"""
