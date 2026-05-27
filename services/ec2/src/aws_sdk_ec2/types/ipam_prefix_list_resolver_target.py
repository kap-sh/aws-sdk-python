"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverTarget``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_long
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_id
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_target_id
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_target_state
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamPrefixListResolverTarget(TypedDict):
    ipam_prefix_list_resolver_target_id: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_target_id.IpamPrefixListResolverTargetId"
    ]
    """<p>The ID of the IPAM prefix list resolver target.</p>"""
    ipam_prefix_list_resolver_target_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IPAM prefix list resolver target.</p>"""
    ipam_prefix_list_resolver_id: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_id.IpamPrefixListResolverId"
    ]
    """<p>The ID of the IPAM prefix list resolver associated with this target.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the IPAM prefix list resolver target.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the managed prefix list associated with this target.</p>"""
    prefix_list_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region where the prefix list associated with this target is located.</p>"""
    desired_version: NotRequired["aws_sdk_ec2.types.boxed_long.BoxedLong"]
    """<p>The desired version of the prefix list that this target should synchronize with.</p>"""
    last_synced_version: NotRequired["aws_sdk_ec2.types.boxed_long.BoxedLong"]
    """<p>The version of the prefix list that was last successfully synchronized by this target.</p>"""
    track_latest_version: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this target automatically tracks the latest version of the prefix list.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message describing the current state of the IPAM prefix list resolver target, including any error information.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_target_state.IpamPrefixListResolverTargetState"
    ]
    """<p>The current state of the IPAM prefix list resolver target. Valid values include <code>create-in-progress</code>, <code>create-complete</code>, <code>create-failed</code>, <code>modify-in-progress</code>, <code>modify-complete</code>, <code>modify-failed</code>, <code>delete-in-progress</code>, <code>delete-complete</code>, and <code>delete-failed</code>.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the IPAM prefix list resolver target.</p>"""
