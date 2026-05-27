"""Generated from Smithy shape ``com.amazonaws.ec2#GetEnabledIpamPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_policy_id
    import aws_sdk_ec2.types.ipam_policy_managed_by


class GetEnabledIpamPolicyResult(TypedDict):
    ipam_policy_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the IPAM policy is enabled.</p>"""
    ipam_policy_id: NotRequired["aws_sdk_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the enabled IPAM policy.</p>"""
    managed_by: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_managed_by.IpamPolicyManagedBy"
    ]
    """<p>The entity that manages the IPAM policy.</p>"""
