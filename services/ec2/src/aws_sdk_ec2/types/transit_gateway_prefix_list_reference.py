"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayPrefixListReference``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.prefix_list_resource_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_prefix_list_attachment
    import aws_sdk_ec2.types.transit_gateway_prefix_list_reference_state
    import aws_sdk_ec2.types.transit_gateway_route_table_id


class TransitGatewayPrefixListReference(TypedDict):
    transit_gateway_route_table_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_id.TransitGatewayRouteTableId"
    ]
    """<p>The ID of the transit gateway route table.</p>"""
    prefix_list_id: NotRequired[
        "aws_sdk_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the prefix list.</p>"""
    prefix_list_owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the prefix list owner.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_prefix_list_reference_state.TransitGatewayPrefixListReferenceState"
    ]
    """<p>The state of the prefix list reference.</p>"""
    blackhole: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether traffic that matches this route is dropped.</p>"""
    transit_gateway_attachment: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_prefix_list_attachment.TransitGatewayPrefixListAttachment"
    ]
    """<p>Information about the transit gateway attachment.</p>"""
