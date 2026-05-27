"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayPrefixListReferenceResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_prefix_list_reference


class DeleteTransitGatewayPrefixListReferenceResult(TypedDict):
    transit_gateway_prefix_list_reference: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_prefix_list_reference.TransitGatewayPrefixListReference"
    ]
    """<p>Information about the deleted prefix list reference.</p>"""
