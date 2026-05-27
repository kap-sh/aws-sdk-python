"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateSecurityGroupVpcResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_vpc_association_state


class DisassociateSecurityGroupVpcResult(TypedDict):
    state: NotRequired[
        "aws_sdk_ec2.types.security_group_vpc_association_state.SecurityGroupVpcAssociationState"
    ]
    """<p>The state of the disassociation.</p>"""
