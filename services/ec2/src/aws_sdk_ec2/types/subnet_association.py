"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_mulitcast_domain_association_state


class SubnetAssociation(TypedDict):
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_mulitcast_domain_association_state.TransitGatewayMulitcastDomainAssociationState"
    ]
    """<p>The state of the subnet association.</p>"""
