"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPolicyAllocationRulesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_document


class ModifyIpamPolicyAllocationRulesResult(TypedDict):
    ipam_policy_document: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_document.IpamPolicyDocument"
    ]
    """<p>The modified IPAM policy containing the updated allocation rules.</p>"""
