"""Generated from Smithy shape ``com.amazonaws.ec2#ManagedPrefixList``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.prefix_list_state
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ManagedPrefixList(TypedDict):
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    address_family: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address version.</p>"""
    state: NotRequired["aws_sdk_ec2.types.prefix_list_state.PrefixListState"]
    """<p>The current state of the prefix list.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state message.</p>"""
    prefix_list_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) for the prefix list.</p>"""
    prefix_list_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the prefix list.</p>"""
    max_entries: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of entries for the prefix list.</p>"""
    version: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The version of the prefix list.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the prefix list.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the owner of the prefix list.</p>"""
    ipam_prefix_list_resolver_target_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the IPAM prefix list resolver target associated with this managed prefix list. When set, this prefix list becomes an IPAM managed prefix list.</p> <p>An IPAM-managed prefix list is a customer-managed prefix list that has been associated with an IPAM prefix list resolver target. When a prefix list becomes IPAM managed, its CIDRs are automatically synchronized based on the IPAM prefix list resolver's CIDR selection rules, and direct CIDR modifications are restricted.</p>"""
    ipam_prefix_list_resolver_sync_enabled: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether synchronization with an IPAM prefix list resolver is enabled for this managed prefix list. When enabled, the prefix list CIDRs are automatically updated based on the resolver's CIDR selection rules.</p>"""
