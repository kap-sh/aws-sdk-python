"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamPrefixListResolverRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.address_family
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_request_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateIpamPrefixListResolverRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM that will serve as the source of the IP address database for CIDR selection. The IPAM must be in the Advanced tier to use this feature.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the IPAM prefix list resolver to help you identify its purpose and configuration.</p>"""
    address_family: NotRequired["aws_sdk_ec2.types.address_family.AddressFamily"]
    """<p>The address family for the IPAM prefix list resolver. Valid values are <code>ipv4</code> and <code>ipv6</code>. You must create separate resolvers for IPv4 and IPv6 CIDRs as they cannot be mixed in the same resolver.</p>"""
    rules: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_request_set.IpamPrefixListResolverRuleRequestSet"
    ]
    """<p>The CIDR selection rules for the resolver.</p> <p>CIDR selection rules define the business logic for selecting CIDRs from IPAM. If a CIDR matches any of the rules, it will be included. If a rule has multiple conditions, the CIDR has to match every condition of that rule. You can create a prefix list resolver without any CIDR selection rules, but it will generate empty versions (containing no CIDRs) until you add rules.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the IPAM prefix list resolver during creation. Tags help you organize and manage your Amazon Web Services resources.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
