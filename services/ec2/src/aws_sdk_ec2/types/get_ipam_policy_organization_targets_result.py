"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPolicyOrganizationTargetsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_organization_target_set
    import aws_sdk_ec2.types.next_token


class GetIpamPolicyOrganizationTargetsResult(TypedDict):
    organization_targets: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_organization_target_set.IpamPolicyOrganizationTargetSet"
    ]
    """<p>The IDs of the Amazon Web Services Organizations targets.</p> <p>A target can be an individual Amazon Web Services account or an entity within an Amazon Web Services Organization to which an IPAM policy can be applied.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""
