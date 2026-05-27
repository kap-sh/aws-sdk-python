"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayMulticastDomainAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_association_list


class GetTransitGatewayMulticastDomainAssociationsResult(TypedDict):
    multicast_domain_associations: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain_association_list.TransitGatewayMulticastDomainAssociationList"
    ]
    """<p>Information about the multicast domain associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
