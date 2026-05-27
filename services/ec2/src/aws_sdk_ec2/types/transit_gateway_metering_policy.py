"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMeteringPolicy``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.transit_gateway_metering_policy_id
    import aws_sdk_ec2.types.transit_gateway_metering_policy_state
    import aws_sdk_ec2.types.value_string_list


class TransitGatewayMeteringPolicy(TypedDict):
    transit_gateway_metering_policy_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_id.TransitGatewayMeteringPolicyId"
    ]
    """<p>The ID of the transit gateway metering policy.</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway associated with the metering policy.</p>"""
    middlebox_attachment_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IDs of the middlebox attachments associated with the metering policy.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_metering_policy_state.TransitGatewayMeteringPolicyState"
    ]
    """<p>The state of the transit gateway metering policy.</p>"""
    update_effective_at: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the metering policy update becomes effective.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the transit gateway metering policy.</p>"""
