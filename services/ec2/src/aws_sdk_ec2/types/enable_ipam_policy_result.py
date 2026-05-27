"""Generated from Smithy shape ``com.amazonaws.ec2#EnableIpamPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_id


class EnableIpamPolicyResult(TypedDict):
    ipam_policy_id: NotRequired["aws_sdk_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy that was enabled.</p>"""
