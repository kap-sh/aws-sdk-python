"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPolicyAllocationRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_policy_allocation_rule_list_request
    import aws_sdk_ec2.types.ipam_policy_id
    import aws_sdk_ec2.types.ipam_policy_resource_type
    import aws_sdk_ec2.types.string


class ModifyIpamPolicyAllocationRulesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_policy_id: NotRequired["aws_sdk_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy whose allocation rules you want to modify.</p>"""
    locale: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The locale for which to modify the allocation rules.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_resource_type.IpamPolicyResourceType"
    ]
    """<p>The resource type for which to modify the allocation rules.</p> <p>The Amazon Web Services service or resource type that can use IP addresses through IPAM policies. Supported services and resource types include:</p> <ul> <li> <p>Elastic IP addresses</p> </li> </ul>"""
    allocation_rules: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_allocation_rule_list_request.IpamPolicyAllocationRuleListRequest"
    ]
    """<p>The new allocation rules to apply to the IPAM policy.</p> <p>Allocation rules are optional configurations within an IPAM policy that map Amazon Web Services resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.</p>"""
