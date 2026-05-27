"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPolicyTable``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_id
    import aws_sdk_ec2.types.transit_gateway_policy_table_id
    import aws_sdk_ec2.types.transit_gateway_policy_table_state


class TransitGatewayPolicyTable(TypedDict):
    transit_gateway_policy_table_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_id.TransitGatewayPolicyTableId"
    ]
    """<p>The ID of the transit gateway policy table.</p>"""
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_policy_table_state.TransitGatewayPolicyTableState"
    ]
    """<p>The state of the transit gateway policy table</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The timestamp when the transit gateway policy table was created.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>he key-value pairs associated with the transit gateway policy table.</p>"""
