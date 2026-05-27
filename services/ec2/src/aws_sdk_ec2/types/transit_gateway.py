"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGateway``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_options
    import aws_sdk_ec2.types.transit_gateway_state


class TransitGateway(TypedDict):
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    transit_gateway_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the transit gateway.</p>"""
    state: NotRequired["aws_sdk_ec2.types.transit_gateway_state.TransitGatewayState"]
    """<p>The state of the transit gateway.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the transit gateway.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the transit gateway.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The creation time.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_options.TransitGatewayOptions"
    ]
    """<p>The transit gateway options.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the transit gateway.</p>"""
