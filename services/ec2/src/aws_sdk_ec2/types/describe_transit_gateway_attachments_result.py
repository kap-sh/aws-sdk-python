"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayAttachmentsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_list


class DescribeTransitGatewayAttachmentsResult(TypedDict):
    transit_gateway_attachments: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_list.TransitGatewayAttachmentList"
    ]
    """<p>Information about the attachments.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
