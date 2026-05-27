"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayPolicyTableAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_policy_table_association_list


class GetTransitGatewayPolicyTableAssociationsResult(TypedDict):
    associations: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_association_list.TransitGatewayPolicyTableAssociationList"
    ]
    """<p>Returns details about the transit gateway policy table association.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
