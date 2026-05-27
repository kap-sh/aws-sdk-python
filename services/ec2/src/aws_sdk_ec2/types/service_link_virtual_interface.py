"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceLinkVirtualInterface``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.outpost_lag_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.service_link_virtual_interface_configuration_state
    import aws_sdk_ec2.types.service_link_virtual_interface_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ServiceLinkVirtualInterface(TypedDict):
    service_link_virtual_interface_id: NotRequired[
        "aws_sdk_ec2.types.service_link_virtual_interface_id.ServiceLinkVirtualInterfaceId"
    ]
    """<p>The ID of the service link virtual interface.</p>"""
    service_link_virtual_interface_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Number (ARN) for the service link virtual interface. </p>"""
    outpost_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Outpost ID for the service link virtual interface.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Outpost Amazon Resource Number (ARN) for the service link virtual interface.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the service link virtual interface..</p>"""
    local_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 address assigned to the local gateway virtual interface on the Outpost side.</p>"""
    peer_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 peer address for the service link virtual interface.</p>"""
    peer_bgp_asn: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The ASN for the Border Gateway Protocol (BGP) associated with the service link virtual interface.</p>"""
    vlan: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The virtual local area network for the service link virtual interface.</p>"""
    outpost_lag_id: NotRequired["aws_sdk_ec2.types.outpost_lag_id.OutpostLagId"]
    """<p>The link aggregation group (LAG) ID for the service link virtual interface.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags associated with the service link virtual interface.</p>"""
    configuration_state: NotRequired[
        "aws_sdk_ec2.types.service_link_virtual_interface_configuration_state.ServiceLinkVirtualInterfaceConfigurationState"
    ]
    """<p>The current state of the service link virtual interface.</p>"""
