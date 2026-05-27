"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyOrganizationTargetSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_organization_target

IpamPolicyOrganizationTargetSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_policy_organization_target.IpamPolicyOrganizationTarget"
]
