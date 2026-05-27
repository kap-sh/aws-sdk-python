"""Generated from Smithy shape ``com.amazonaws.ec2#SecondarySubnetIpv4CidrBlockAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_subnet_cidr_association_id
    import aws_sdk_ec2.types.secondary_subnet_cidr_block_association_state
    import aws_sdk_ec2.types.string


class SecondarySubnetIpv4CidrBlockAssociation(TypedDict):
    association_id: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_cidr_association_id.SecondarySubnetCidrAssociationId"
    ]
    """<p>The association ID for the IPv4 CIDR block.</p>"""
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR block.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_cidr_block_association_state.SecondarySubnetCidrBlockAssociationState"
    ]
    """<p>The state of the CIDR block association.</p>"""
    state_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the current state of the CIDR block association.</p>"""
