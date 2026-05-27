"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolver``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_family
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_id
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_state
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_version_creation_status
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamPrefixListResolver(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the IPAM prefix list resolver.</p>"""
    ipam_prefix_list_resolver_id: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_id.IpamPrefixListResolverId"
    ]
    """<p>The ID of the IPAM prefix list resolver.</p>"""
    ipam_prefix_list_resolver_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IPAM prefix list resolver.</p>"""
    ipam_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IPAM associated with this resolver.</p>"""
    ipam_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region where the associated IPAM is located.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the IPAM prefix list resolver.</p>"""
    address_family: NotRequired["aws_sdk_ec2.types.address_family.AddressFamily"]
    """<p>The address family (IPv4 or IPv6) for the IPAM prefix list resolver.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_state.IpamPrefixListResolverState"
    ]
    """<p>The current state of the IPAM prefix list resolver. Valid values include <code>create-in-progress</code>, <code>create-complete</code>, <code>create-failed</code>, <code>modify-in-progress</code>, <code>modify-complete</code>, <code>modify-failed</code>, <code>delete-in-progress</code>, <code>delete-complete</code>, and <code>delete-failed</code>.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the IPAM prefix list resolver.</p>"""
    last_version_creation_status: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_version_creation_status.IpamPrefixListResolverVersionCreationStatus"
    ]
    """<p>The status for the last time a version was created.</p> <p>Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.</p>"""
    last_version_creation_status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message for the last time a version was created.</p> <p>Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.</p>"""
