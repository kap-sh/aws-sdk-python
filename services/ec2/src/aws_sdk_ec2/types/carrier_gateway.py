"""Generated from Smithy shape ``com.amazonaws.ec2#CarrierGateway``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.carrier_gateway_id
    import aws_sdk_ec2.types.carrier_gateway_state
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_id


class CarrierGateway(TypedDict):
    carrier_gateway_id: NotRequired[
        "aws_sdk_ec2.types.carrier_gateway_id.CarrierGatewayId"
    ]
    """<p>The ID of the carrier gateway.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC associated with the carrier gateway.</p>"""
    state: NotRequired["aws_sdk_ec2.types.carrier_gateway_state.CarrierGatewayState"]
    """<p>The state of the carrier gateway.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the carrier gateway.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the carrier gateway.</p>"""
