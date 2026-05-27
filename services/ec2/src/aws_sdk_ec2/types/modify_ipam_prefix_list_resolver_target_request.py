"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPrefixListResolverTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_boolean
    import aws_sdk_ec2.types.boxed_long
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_target_id
    import aws_sdk_ec2.types.string


class ModifyIpamPrefixListResolverTargetRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_prefix_list_resolver_target_id: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_target_id.IpamPrefixListResolverTargetId"
    ]
    """<p>The ID of the IPAM prefix list resolver target to modify.</p>"""
    desired_version: NotRequired["aws_sdk_ec2.types.boxed_long.BoxedLong"]
    """<p>The desired version of the prefix list to target. This allows you to pin the target to a specific version.</p>"""
    track_latest_version: NotRequired["aws_sdk_ec2.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether the resolver target should automatically track the latest version of the prefix list. When enabled, the target will always synchronize with the most current version.</p> <p>Choose this for automatic updates when you want your prefix lists to stay current with infrastructure changes without manual intervention.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
