"""Generated from Smithy shape ``com.amazonaws.ec2#NatGateway``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.auto_provision_zones_state
    import aws_sdk_ec2.types.auto_scaling_ips_state
    import aws_sdk_ec2.types.availability_mode
    import aws_sdk_ec2.types.connectivity_type
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.nat_gateway_address_list
    import aws_sdk_ec2.types.nat_gateway_attached_appliance_list
    import aws_sdk_ec2.types.nat_gateway_state
    import aws_sdk_ec2.types.provisioned_bandwidth
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class NatGateway(TypedDict):
    create_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time the NAT gateway was created.</p>"""
    delete_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time the NAT gateway was deleted, if applicable.</p>"""
    failure_code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If the NAT gateway could not be created, specifies the error code for the failure. (<code>InsufficientFreeAddressesInSubnet</code> | <code>Gateway.NotAttached</code> | <code>InvalidAllocationID.NotFound</code> | <code>Resource.AlreadyAssociated</code> | <code>InternalError</code> | <code>InvalidSubnetID.NotFound</code>)</p>"""
    failure_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If the NAT gateway could not be created, specifies the error message for the failure, that corresponds to the error code.</p> <ul> <li> <p>For InsufficientFreeAddressesInSubnet: \"Subnet has insufficient free addresses to create this NAT gateway\"</p> </li> <li> <p>For Gateway.NotAttached: \"Network vpc-xxxxxxxx has no Internet gateway attached\"</p> </li> <li> <p>For InvalidAllocationID.NotFound: \"Elastic IP address eipalloc-xxxxxxxx could not be associated with this NAT gateway\"</p> </li> <li> <p>For Resource.AlreadyAssociated: \"Elastic IP address eipalloc-xxxxxxxx is already associated\"</p> </li> <li> <p>For InternalError: \"Network interface eni-xxxxxxxx, created and used internally by this NAT gateway is in an invalid state. Please try again.\"</p> </li> <li> <p>For InvalidSubnetID.NotFound: \"The specified subnet subnet-xxxxxxxx does not exist or could not be found.\"</p> </li> </ul>"""
    nat_gateway_addresses: NotRequired[
        "aws_sdk_ec2.types.nat_gateway_address_list.NatGatewayAddressList"
    ]
    """<p>Information about the IP addresses and network interface associated with the NAT gateway.</p>"""
    nat_gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the NAT gateway.</p>"""
    provisioned_bandwidth: NotRequired[
        "aws_sdk_ec2.types.provisioned_bandwidth.ProvisionedBandwidth"
    ]
    """<p>Reserved. If you need to sustain traffic greater than the <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-gateways\">documented limits</a>, contact Amazon Web Services Support.</p>"""
    state: NotRequired["aws_sdk_ec2.types.nat_gateway_state.NatGatewayState"]
    """<p>The state of the NAT gateway.</p> <ul> <li> <p> <code>pending</code>: The NAT gateway is being created and is not ready to process traffic.</p> </li> <li> <p> <code>failed</code>: The NAT gateway could not be created. Check the <code>failureCode</code> and <code>failureMessage</code> fields for the reason.</p> </li> <li> <p> <code>available</code>: The NAT gateway is able to process traffic. This status remains until you delete the NAT gateway, and does not indicate the health of the NAT gateway.</p> </li> <li> <p> <code>deleting</code>: The NAT gateway is in the process of being terminated and may still be processing traffic.</p> </li> <li> <p> <code>deleted</code>: The NAT gateway has been terminated and is no longer processing traffic.</p> </li> </ul>"""
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subnet in which the NAT gateway is located.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC in which the NAT gateway is located.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags for the NAT gateway.</p>"""
    connectivity_type: NotRequired[
        "aws_sdk_ec2.types.connectivity_type.ConnectivityType"
    ]
    """<p>Indicates whether the NAT gateway supports public or private connectivity.</p>"""
    availability_mode: NotRequired[
        "aws_sdk_ec2.types.availability_mode.AvailabilityMode"
    ]
    """<p>Indicates whether this is a zonal (single-AZ) or regional (multi-AZ) NAT gateway.</p> <p>A zonal NAT gateway is a NAT Gateway that provides redundancy and scalability within a single availability zone. A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html\">Regional NAT gateways for automatic multi-AZ expansion</a> in the <i>Amazon VPC User Guide</i>.</p>"""
    auto_scaling_ips: NotRequired[
        "aws_sdk_ec2.types.auto_scaling_ips_state.AutoScalingIpsState"
    ]
    """<p>For regional NAT gateways only: Indicates whether Amazon Web Services automatically allocates additional Elastic IP addresses (EIPs) in an AZ when the NAT gateway needs more ports due to increased concurrent connections to a single destination from that AZ.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html\">Regional NAT gateways for automatic multi-AZ expansion</a> in the <i>Amazon VPC User Guide</i>.</p>"""
    auto_provision_zones: NotRequired[
        "aws_sdk_ec2.types.auto_provision_zones_state.AutoProvisionZonesState"
    ]
    """<p>For regional NAT gateways only: Indicates whether Amazon Web Services automatically manages AZ coverage. When enabled, the NAT gateway associates EIPs in all AZs where your VPC has subnets to handle outbound NAT traffic, expands to new AZs when you create subnets there, and retracts from AZs where you've removed all subnets. When disabled, you must manually manage which AZs the NAT gateway supports and their corresponding EIPs.</p> <p>A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html\">Regional NAT gateways for automatic multi-AZ expansion</a> in the <i>Amazon VPC User Guide</i>.</p>"""
    attached_appliances: NotRequired[
        "aws_sdk_ec2.types.nat_gateway_attached_appliance_list.NatGatewayAttachedApplianceList"
    ]
    """<p>The proxy appliances attached to the NAT Gateway for filtering and inspecting traffic to prevent data exfiltration.</p>"""
    route_table_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>For regional NAT gateways only, this is the ID of the NAT gateway.</p>"""
