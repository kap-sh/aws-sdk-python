"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryNetworkIpv4CidrBlockAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_network_ipv4_cidr_block_association

SecondaryNetworkIpv4CidrBlockAssociationList: TypeAlias = list[
    "aws_sdk_ec2.types.secondary_network_ipv4_cidr_block_association.SecondaryNetworkIpv4CidrBlockAssociation"
]
