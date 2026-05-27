"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayAddress``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.nat_gateway_address_status
    import aws_sdk_ec2.types.string


class NatGatewayAddress(TypedDict):
    allocation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>[Public NAT gateway only] The allocation ID of the Elastic IP address that's associated with the NAT gateway.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface associated with the NAT gateway.</p>"""
    private_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The private IP address associated with the NAT gateway.</p>"""
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>[Public NAT gateway only] The Elastic IP address associated with the NAT gateway.</p>"""
    association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>[Public NAT gateway only] The association ID of the Elastic IP address that's associated with the NAT gateway.</p>"""
    is_primary: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Defines if the IP address is the primary address.</p>"""
    failure_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The address failure message.</p>"""
    status: NotRequired[
        "aws_sdk_ec2.types.nat_gateway_address_status.NatGatewayAddressStatus"
    ]
    """<p>The address status.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone where this Elastic IP address (EIP) is being used to handle outbound NAT traffic.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone where this Elastic IP address (EIP) is being used to handle outbound NAT traffic. Use this instead of AvailabilityZone for consistent identification of AZs across Amazon Web Services Regions.</p>"""
