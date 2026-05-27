"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConfigurationInputStructure``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_availability_zone_id_set
    import aws_sdk_ec2.types.client_vpn_availability_zone_set
    import aws_sdk_ec2.types.transit_gateway_id


class TransitGatewayConfigurationInputStructure(TypedDict):
    transit_gateway_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_id.TransitGatewayId"
    ]
    """<p>The ID of the Transit Gateway to associate with the Client VPN endpoint.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.client_vpn_availability_zone_set.ClientVpnAvailabilityZoneSet"
    ]
    """<p>The Availability Zone names for the Transit Gateway association. You can specify up to the maximum number of Availability Zones supported by the Transit Gateway. You cannot specify both <code>AvailabilityZones</code> and <code>AvailabilityZoneIds</code>.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_ec2.types.client_vpn_availability_zone_id_set.ClientVpnAvailabilityZoneIdSet"
    ]
    """<p>The Availability Zone IDs for the Transit Gateway association. You can specify up to the maximum number of Availability Zones supported by the Transit Gateway. You cannot specify both <code>AvailabilityZones</code> and <code>AvailabilityZoneIds</code>.</p>"""
