"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastRegisteredGroupMembers``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class TransitGatewayMulticastRegisteredGroupMembers(TypedDict):
    transit_gateway_multicast_domain_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the transit gateway multicast domain.</p>"""
    registered_network_interface_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The ID of the registered network interfaces.</p>"""
    group_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IP address assigned to the transit gateway multicast group.</p>"""
