"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPrefixListResolverRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_id
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_request_set
    import aws_sdk_ec2.types.string


class ModifyIpamPrefixListResolverRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_prefix_list_resolver_id: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_id.IpamPrefixListResolverId"
    ]
    """<p>The ID of the IPAM prefix list resolver to modify.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A new description for the IPAM prefix list resolver.</p>"""
    rules: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_request_set.IpamPrefixListResolverRuleRequestSet"
    ]
    """<p>The updated CIDR selection rules for the resolver. These rules replace the existing rules entirely.</p>"""
