"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamPrefixListResolverTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.boxed_long
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateIpamPrefixListResolverTargetRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_prefix_list_resolver_id: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_id.IpamPrefixListResolverId"
    ]
    """<p>The ID of the IPAM prefix list resolver that will manage the synchronization of CIDRs to the target prefix list.</p>"""
    prefix_list_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the managed prefix list that will be synchronized with CIDRs selected by the IPAM prefix list resolver. This prefix list becomes an IPAM managed prefix list.</p> <p>An IPAM-managed prefix list is a customer-managed prefix list that has been associated with an IPAM prefix list resolver target. When a prefix list becomes IPAM managed, its CIDRs are automatically synchronized based on the IPAM prefix list resolver's CIDR selection rules, and direct CIDR modifications are restricted.</p>"""
    prefix_list_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region where the prefix list is located. This is required when referencing a prefix list in a different Region.</p>"""
    desired_version: NotRequired["aws_sdk_ec2.types.boxed_long.BoxedLong"]
    """<p>The specific version of the prefix list to target. If not specified, the resolver will target the latest version.</p>"""
    track_latest_version: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the resolver target should automatically track the latest version of the prefix list. When enabled, the target will always synchronize with the most current version of the prefix list.</p> <p>Choose this for automatic updates when you want your prefix lists to stay current with infrastructure changes without manual intervention.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the IPAM prefix list resolver target during creation. Tags help you organize and manage your Amazon Web Services resources.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
