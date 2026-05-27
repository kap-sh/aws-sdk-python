"""Generated from Smithy shape ``com.amazonaws.ec2#EgressOnlyInternetGateway``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.egress_only_internet_gateway_id
    import aws_sdk_ec2.types.internet_gateway_attachment_list
    import aws_sdk_ec2.types.tag_list


class EgressOnlyInternetGateway(TypedDict):
    attachments: NotRequired[
        "aws_sdk_ec2.types.internet_gateway_attachment_list.InternetGatewayAttachmentList"
    ]
    """<p>Information about the attachment of the egress-only internet gateway.</p>"""
    egress_only_internet_gateway_id: NotRequired[
        "aws_sdk_ec2.types.egress_only_internet_gateway_id.EgressOnlyInternetGatewayId"
    ]
    """<p>The ID of the egress-only internet gateway.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the egress-only internet gateway.</p>"""
