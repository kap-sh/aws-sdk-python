"""Generated from Smithy shape ``com.amazonaws.ec2#SearchTransitGatewayMulticastGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_multicast_group_list


class SearchTransitGatewayMulticastGroupsResult(TypedDict):
    multicast_groups: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_group_list.TransitGatewayMulticastGroupList"
    ]
    """<p>Information about the transit gateway multicast group.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
