"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroupReferencesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_references


class DescribeSecurityGroupReferencesResult(TypedDict):
    security_group_reference_set: NotRequired[
        "aws_sdk_ec2.types.security_group_references.SecurityGroupReferences"
    ]
    """<p>Information about the VPCs with the referencing security groups.</p>"""
