"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGateway``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class LocalGateway(TypedDict):
    local_gateway_id: NotRequired["aws_sdk_ec2.types.local_gateway_id.LocalGatewayId"]
    """<p>The ID of the local gateway.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the local gateway.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The state of the local gateway.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the local gateway.</p>"""
