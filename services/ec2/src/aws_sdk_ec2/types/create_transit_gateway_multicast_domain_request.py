"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayMulticastDomainRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.create_transit_gateway_multicast_domain_request_options
    import aws_sdk_ec2.types.tag_specification_list
    import aws_sdk_ec2.types.transit_gateway_id


class CreateTransitGatewayMulticastDomainRequest(TypedDict):
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the transit gateway.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.create_transit_gateway_multicast_domain_request_options.CreateTransitGatewayMulticastDomainRequestOptions"
    ]
    """<p>The options for the transit gateway multicast domain.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags for the transit gateway multicast domain.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
