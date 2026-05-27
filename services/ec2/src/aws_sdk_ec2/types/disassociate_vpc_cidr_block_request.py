"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateVpcCidrBlockRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_cidr_association_id


class DisassociateVpcCidrBlockRequest(TypedDict):
    association_id: NotRequired[
        "aws_sdk_ec2.types.vpc_cidr_association_id.VpcCidrAssociationId"
    ]
    """<p>The association ID for the CIDR block.</p>"""
