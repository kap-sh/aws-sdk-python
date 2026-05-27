"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateSubnetCidrBlockRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.subnet_cidr_association_id


class DisassociateSubnetCidrBlockRequest(TypedDict):
    association_id: NotRequired[
        "aws_sdk_ec2.types.subnet_cidr_association_id.SubnetCidrAssociationId"
    ]
    """<p>The association ID for the CIDR block.</p>"""
