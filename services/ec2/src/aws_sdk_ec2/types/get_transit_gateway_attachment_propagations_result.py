"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayAttachmentPropagationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_propagation_list


class GetTransitGatewayAttachmentPropagationsResult(TypedDict):
    transit_gateway_attachment_propagations: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_propagation_list.TransitGatewayAttachmentPropagationList"
    ]
    """<p>Information about the propagation route tables.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
