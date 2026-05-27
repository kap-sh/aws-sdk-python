"""Generated from Smithy shape ``com.amazonaws.ec2#TargetNetwork``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.association_status
    import aws_sdk_ec2.types.client_vpn_availability_zone_id_set
    import aws_sdk_ec2.types.client_vpn_availability_zone_set
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class TargetNetwork(TypedDict):
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the association.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC in which the target network (subnet) is located.</p>"""
    target_network_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet specified as the target network.</p>"""
    client_vpn_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint with which the target network is associated.</p>"""
    status: NotRequired["aws_sdk_ec2.types.association_status.AssociationStatus"]
    """<p>The current state of the target network association.</p>"""
    security_groups: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The IDs of the security groups applied to the target network association.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.client_vpn_availability_zone_set.ClientVpnAvailabilityZoneSet"
    ]
    """<p>The Availability Zone names for the target network association, if the Client VPN endpoint uses a Transit Gateway.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_ec2.types.client_vpn_availability_zone_id_set.ClientVpnAvailabilityZoneIdSet"
    ]
    """<p>The Availability Zone IDs for the target network association, if the Client VPN endpoint uses a Transit Gateway.</p>"""
