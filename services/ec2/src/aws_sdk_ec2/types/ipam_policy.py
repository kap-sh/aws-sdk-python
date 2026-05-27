"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicy``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.ipam_policy_id
    import aws_sdk_ec2.types.ipam_policy_state
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamPolicy(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The account ID that owns the IPAM policy.</p>"""
    ipam_policy_id: NotRequired["aws_sdk_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy.</p>"""
    ipam_policy_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IPAM policy.</p>"""
    ipam_policy_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region of the IPAM policy.</p>"""
    state: NotRequired["aws_sdk_ec2.types.ipam_policy_state.IpamPolicyState"]
    """<p>The state of the IPAM policy.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message about the state of the IPAM policy.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the IPAM policy.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM this policy belongs to.</p>"""
