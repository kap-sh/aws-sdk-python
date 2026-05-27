"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleConditionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_operation
    import aws_sdk_ec2.types.request_ipam_resource_tag
    import aws_sdk_ec2.types.string


class IpamPrefixListResolverRuleConditionRequest(TypedDict):
    operation: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_operation.IpamPrefixListResolverRuleConditionOperation"
    ]
    """<p>The operation to perform when evaluating this condition.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the IPAM pool to match against. This condition selects CIDRs that belong to the specified IPAM pool.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services resource to match against. This condition selects CIDRs associated with the specified resource.</p>"""
    resource_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID that owns the resources to match against. This condition selects CIDRs from resources owned by the specified account.</p>"""
    resource_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region where the resources are located. This condition selects CIDRs from resources in the specified Region.</p>"""
    resource_tag: NotRequired[
        "aws_sdk_ec2.types.request_ipam_resource_tag.RequestIpamResourceTag"
    ]
    """<p>A tag key-value pair to match against. This condition selects CIDRs from resources that have the specified tag.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A CIDR block to match against. This condition selects CIDRs that fall within or match the specified CIDR range.</p>"""
