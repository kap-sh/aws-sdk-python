"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyDocumentSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_document

IpamPolicyDocumentSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_policy_document.IpamPolicyDocument"
]
