"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptTransitGatewayMulticastDomainAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_associations


class AcceptTransitGatewayMulticastDomainAssociationsResult(TypedDict):
    associations: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain_associations.TransitGatewayMulticastDomainAssociations"
    ]
    """<p>Information about the multicast domain associations.</p>"""
