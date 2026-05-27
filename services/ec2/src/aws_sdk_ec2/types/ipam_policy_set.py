"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicySet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy

IpamPolicySet: TypeAlias = list["aws_sdk_ec2.types.ipam_policy.IpamPolicy"]
