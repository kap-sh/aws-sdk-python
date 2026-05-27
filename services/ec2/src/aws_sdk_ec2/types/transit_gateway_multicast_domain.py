"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomain``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_options
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_state


class TransitGatewayMulticastDomain(TypedDict):
    transit_gateway_multicast_domain_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    transit_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway.</p>"""
    transit_gateway_multicast_domain_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the transit gateway multicast domain.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The ID of the Amazon Web Services account that owns the transit gateway multicast domain.</p>"""
    options: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain_options.TransitGatewayMulticastDomainOptions"
    ]
    """<p>The options for the transit gateway multicast domain.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain_state.TransitGatewayMulticastDomainState"
    ]
    """<p>The state of the transit gateway multicast domain.</p>"""
    creation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time the transit gateway multicast domain was created.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the transit gateway multicast domain.</p>"""
