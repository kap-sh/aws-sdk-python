"""Generated from Smithy shape ``com.amazonaws.ec2#InternetGateway``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.internet_gateway_attachment_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class InternetGateway(TypedDict):
    attachments: NotRequired[
        "aws_sdk_ec2.types.internet_gateway_attachment_list.InternetGatewayAttachmentList"
    ]
    """<p>Any VPCs attached to the internet gateway.</p>"""
    internet_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the internet gateway.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the internet gateway.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the internet gateway.</p>"""
