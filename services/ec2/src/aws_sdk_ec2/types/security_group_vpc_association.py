"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupVpcAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_id
    import aws_sdk_ec2.types.security_group_vpc_association_state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_id


class SecurityGroupVpcAssociation(TypedDict):
    group_id: NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The association's security group ID.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The association's VPC ID.</p>"""
    vpc_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the VPC.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.security_group_vpc_association_state.SecurityGroupVpcAssociationState"
    ]
    """<p>The association's state.</p>"""
    state_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The association's state reason.</p>"""
    group_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the security group.</p>"""
