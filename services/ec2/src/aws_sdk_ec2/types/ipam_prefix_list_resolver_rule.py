"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_set
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_type
    import aws_sdk_ec2.types.ipam_resource_type
    import aws_sdk_ec2.types.ipam_scope_id
    import aws_sdk_ec2.types.string


class IpamPrefixListResolverRule(TypedDict):
    rule_type: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_type.IpamPrefixListResolverRuleType"
    ]
    """<p>The type of CIDR selection rule. Valid values include <code>include</code> for selecting CIDRs that match the conditions, and <code>exclude</code> for excluding CIDRs that match the conditions.</p>"""
    static_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A fixed list of CIDRs that do not change (like a manual list replicated across Regions).</p>"""
    ipam_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the IPAM scope from which to select CIDRs. This determines whether to select from public or private IP address space.</p>"""
    resource_type: NotRequired["aws_sdk_ec2.types.ipam_resource_type.IpamResourceType"]
    """<p>For rules of type <code>ipam-resource-cidr</code>, this is the resource type.</p>"""
    conditions: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_set.IpamPrefixListResolverRuleConditionSet"
    ]
    """<p>The conditions that determine which CIDRs are selected by this rule. Conditions specify criteria such as resource type, tags, account IDs, and Regions.</p>"""
