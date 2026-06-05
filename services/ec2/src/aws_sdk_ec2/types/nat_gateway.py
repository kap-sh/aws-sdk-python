"""Generated from Smithy shape ``com.amazonaws.ec2#NatGateway``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NatGateway, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "create_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{prefix}.CreateTime"
        )
    if "delete_time" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["delete_time"], pairs, f"{prefix}.DeleteTime"
        )
    if "failure_code" in value:
        pairs.append((f"{prefix}.FailureCode", str(value["failure_code"])))
    if "failure_message" in value:
        pairs.append((f"{prefix}.FailureMessage", str(value["failure_message"])))
    if "nat_gateway_addresses" in value:
        import aws_sdk_ec2.types.nat_gateway_address_list

        aws_sdk_ec2.types.nat_gateway_address_list.serialize_ec2_query(
            value["nat_gateway_addresses"], pairs, f"{prefix}.NatGatewayAddressSet"
        )
    if "nat_gateway_id" in value:
        pairs.append((f"{prefix}.NatGatewayId", str(value["nat_gateway_id"])))
    if "provisioned_bandwidth" in value:
        import aws_sdk_ec2.types.provisioned_bandwidth

        aws_sdk_ec2.types.provisioned_bandwidth.serialize_ec2_query(
            value["provisioned_bandwidth"], pairs, f"{prefix}.ProvisionedBandwidth"
        )
    if "state" in value:
        import aws_sdk_ec2.types.nat_gateway_state

        aws_sdk_ec2.types.nat_gateway_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "connectivity_type" in value:
        import aws_sdk_ec2.types.connectivity_type

        aws_sdk_ec2.types.connectivity_type.serialize_ec2_query(
            value["connectivity_type"], pairs, f"{prefix}.ConnectivityType"
        )
    if "availability_mode" in value:
        import aws_sdk_ec2.types.availability_mode

        aws_sdk_ec2.types.availability_mode.serialize_ec2_query(
            value["availability_mode"], pairs, f"{prefix}.AvailabilityMode"
        )
    if "auto_scaling_ips" in value:
        import aws_sdk_ec2.types.auto_scaling_ips_state

        aws_sdk_ec2.types.auto_scaling_ips_state.serialize_ec2_query(
            value["auto_scaling_ips"], pairs, f"{prefix}.AutoScalingIps"
        )
    if "auto_provision_zones" in value:
        import aws_sdk_ec2.types.auto_provision_zones_state

        aws_sdk_ec2.types.auto_provision_zones_state.serialize_ec2_query(
            value["auto_provision_zones"], pairs, f"{prefix}.AutoProvisionZones"
        )
    if "attached_appliances" in value:
        import aws_sdk_ec2.types.nat_gateway_attached_appliance_list

        aws_sdk_ec2.types.nat_gateway_attached_appliance_list.serialize_ec2_query(
            value["attached_appliances"], pairs, f"{prefix}.AttachedApplianceSet"
        )
    if "route_table_id" in value:
        pairs.append((f"{prefix}.RouteTableId", str(value["route_table_id"])))


def deserialize_ec2_query(el: Element) -> NatGateway:
    out: NatGateway = {}  # type: ignore[typeddict-item]
    child_create_time = el.find("CreateTime")
    if child_create_time is not None:
        import aws_sdk_ec2.types.date_time

        out["create_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_create_time
        )
    child_delete_time = el.find("DeleteTime")
    if child_delete_time is not None:
        import aws_sdk_ec2.types.date_time

        out["delete_time"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_delete_time
        )
    child_failure_code = el.find("FailureCode")
    if child_failure_code is not None:
        out["failure_code"] = str(child_failure_code.text or "")
    child_failure_message = el.find("FailureMessage")
    if child_failure_message is not None:
        out["failure_message"] = str(child_failure_message.text or "")
    if el.find("NatGatewayAddressSet") is not None:
        import aws_sdk_ec2.types.nat_gateway_address_list

        out["nat_gateway_addresses"] = (
            aws_sdk_ec2.types.nat_gateway_address_list.deserialize_ec2_query(
                el, "NatGatewayAddressSet"
            )
        )
    child_nat_gateway_id = el.find("NatGatewayId")
    if child_nat_gateway_id is not None:
        out["nat_gateway_id"] = str(child_nat_gateway_id.text or "")
    child_provisioned_bandwidth = el.find("ProvisionedBandwidth")
    if child_provisioned_bandwidth is not None:
        import aws_sdk_ec2.types.provisioned_bandwidth

        out["provisioned_bandwidth"] = (
            aws_sdk_ec2.types.provisioned_bandwidth.deserialize_ec2_query(
                child_provisioned_bandwidth
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.nat_gateway_state

        out["state"] = aws_sdk_ec2.types.nat_gateway_state.deserialize_ec2_query(
            child_state
        )
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_connectivity_type = el.find("ConnectivityType")
    if child_connectivity_type is not None:
        import aws_sdk_ec2.types.connectivity_type

        out["connectivity_type"] = (
            aws_sdk_ec2.types.connectivity_type.deserialize_ec2_query(
                child_connectivity_type
            )
        )
    child_availability_mode = el.find("AvailabilityMode")
    if child_availability_mode is not None:
        import aws_sdk_ec2.types.availability_mode

        out["availability_mode"] = (
            aws_sdk_ec2.types.availability_mode.deserialize_ec2_query(
                child_availability_mode
            )
        )
    child_auto_scaling_ips = el.find("AutoScalingIps")
    if child_auto_scaling_ips is not None:
        import aws_sdk_ec2.types.auto_scaling_ips_state

        out["auto_scaling_ips"] = (
            aws_sdk_ec2.types.auto_scaling_ips_state.deserialize_ec2_query(
                child_auto_scaling_ips
            )
        )
    child_auto_provision_zones = el.find("AutoProvisionZones")
    if child_auto_provision_zones is not None:
        import aws_sdk_ec2.types.auto_provision_zones_state

        out["auto_provision_zones"] = (
            aws_sdk_ec2.types.auto_provision_zones_state.deserialize_ec2_query(
                child_auto_provision_zones
            )
        )
    if el.find("AttachedApplianceSet") is not None:
        import aws_sdk_ec2.types.nat_gateway_attached_appliance_list

        out["attached_appliances"] = (
            aws_sdk_ec2.types.nat_gateway_attached_appliance_list.deserialize_ec2_query(
                el, "AttachedApplianceSet"
            )
        )
    child_route_table_id = el.find("RouteTableId")
    if child_route_table_id is not None:
        out["route_table_id"] = str(child_route_table_id.text or "")
    return out
