"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyDocument``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_allocation_rule_list
    import aws_sdk_ec2.types.ipam_policy_id
    import aws_sdk_ec2.types.ipam_policy_resource_type
    import aws_sdk_ec2.types.string


class IpamPolicyDocument(TypedDict):
    ipam_policy_id: NotRequired["aws_sdk_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy.</p>"""
    locale: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The locale of the IPAM policy document.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_resource_type.IpamPolicyResourceType"
    ]
    """<p>The resource type of the IPAM policy document.</p> <p>The Amazon Web Services service or resource type that can use IP addresses through IPAM policies. Supported services and resource types include:</p> <ul> <li> <p>Elastic IP addresses</p> </li> </ul>"""
    allocation_rules: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_allocation_rule_list.IpamPolicyAllocationRuleList"
    ]
    """<p>The allocation rules in the IPAM policy document.</p> <p>Allocation rules are optional configurations within an IPAM policy that map Amazon Web Services resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.</p>"""
