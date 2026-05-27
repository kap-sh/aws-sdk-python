"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyAllocationRuleListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_allocation_rule_request

IpamPolicyAllocationRuleListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_policy_allocation_rule_request.IpamPolicyAllocationRuleRequest"
]
