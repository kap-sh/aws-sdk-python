"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamPrefixListResolverTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_target_id


class DeleteIpamPrefixListResolverTargetRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_prefix_list_resolver_target_id: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_target_id.IpamPrefixListResolverTargetId"
    ]
    """<p>The ID of the IPAM prefix list resolver target to delete.</p>"""
