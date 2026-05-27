"""Generated from Smithy shape ``com.amazonaws.ec2#OutpostLag``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface_id_set
    import aws_sdk_ec2.types.outpost_lag_id
    import aws_sdk_ec2.types.service_link_virtual_interface_id_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class OutpostLag(TypedDict):
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Number (ARN) of the Outpost LAG.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Outpost LAG owner.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of the Outpost LAG.</p>"""
    outpost_lag_id: NotRequired["aws_sdk_ec2.types.outpost_lag_id.OutpostLagId"]
    """<p>The ID of the Outpost LAG.</p>"""
    local_gateway_virtual_interface_ids: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_id_set.LocalGatewayVirtualInterfaceIdSet"
    ]
    """<p>The IDs of the local gateway virtual interfaces associated with the Outpost LAG.</p>"""
    service_link_virtual_interface_ids: NotRequired[
        "aws_sdk_ec2.types.service_link_virtual_interface_id_set.ServiceLinkVirtualInterfaceIdSet"
    ]
    """<p>The service link virtual interface IDs associated with the Outpost LAG.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags associated with the Outpost LAG.</p>"""
