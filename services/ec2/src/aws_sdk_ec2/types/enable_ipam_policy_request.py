"""Generated from Smithy shape ``com.amazonaws.ec2#EnableIpamPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_policy_id
    import aws_sdk_ec2.types.string


class EnableIpamPolicyRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_policy_id: NotRequired["aws_sdk_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy to enable.</p>"""
    organization_target_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A target can be an individual Amazon Web Services account or an entity within an Amazon Web Services Organization to which an IPAM policy can be applied.</p> <p>The ID of the Amazon Web Services Organizations target for which to enable the IPAM policy. This parameter is required only when IPAM is integrated with Amazon Web Services Organizations. When IPAM is not integrated with Amazon Web Services Organizations, omit this parameter and the policy will apply to the current account.</p>"""
