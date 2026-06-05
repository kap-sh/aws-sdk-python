"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateNatGatewayAddressRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_id_list
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ip_list
    import aws_sdk_ec2.types.nat_gateway_id


class AssociateNatGatewayAddressRequest(TypedDict):
    nat_gateway_id: NotRequired["aws_sdk_ec2.types.nat_gateway_id.NatGatewayId"]
    """<p>The ID of the NAT gateway.</p>"""
    allocation_ids: NotRequired["aws_sdk_ec2.types.allocation_id_list.AllocationIdList"]
    """<p>The allocation IDs of EIPs that you want to associate with your NAT gateway.</p>"""
    private_ip_addresses: NotRequired["aws_sdk_ec2.types.ip_list.IpList"]
    """<p>The private IPv4 addresses that you want to assign to the NAT gateway.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>For regional NAT gateways only: The Availability Zone where you want to associate an Elastic IP address (EIP). The regional NAT gateway uses a separate EIP in each AZ to handle outbound NAT traffic from that AZ.</p> <p>A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>For regional NAT gateways only: The ID of the Availability Zone where you want to associate an Elastic IP address (EIP). The regional NAT gateway uses a separate EIP in each AZ to handle outbound NAT traffic from that AZ. Use this instead of AvailabilityZone for consistent identification of AZs across Amazon Web Services Regions. </p> <p>A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateNatGatewayAddressRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "nat_gateway_id" in value:
        pairs.append((f"{prefix}.NatGatewayId", str(value["nat_gateway_id"])))
    if "allocation_ids" in value:
        import aws_sdk_ec2.types.allocation_id_list

        aws_sdk_ec2.types.allocation_id_list.serialize_ec2_query(
            value["allocation_ids"], pairs, f"{prefix}.AllocationIds"
        )
    if "private_ip_addresses" in value:
        import aws_sdk_ec2.types.ip_list

        aws_sdk_ec2.types.ip_list.serialize_ec2_query(
            value["private_ip_addresses"], pairs, f"{prefix}.PrivateIpAddresses"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> AssociateNatGatewayAddressRequest:
    out: AssociateNatGatewayAddressRequest = {}  # type: ignore[typeddict-item]
    child_nat_gateway_id = el.find("NatGatewayId")
    if child_nat_gateway_id is not None:
        out["nat_gateway_id"] = str(child_nat_gateway_id.text or "")
    if el.find("AllocationIds") is not None:
        import aws_sdk_ec2.types.allocation_id_list

        out["allocation_ids"] = (
            aws_sdk_ec2.types.allocation_id_list.deserialize_ec2_query(
                el, "AllocationIds"
            )
        )
    if el.find("PrivateIpAddresses") is not None:
        import aws_sdk_ec2.types.ip_list

        out["private_ip_addresses"] = aws_sdk_ec2.types.ip_list.deserialize_ec2_query(
            el, "PrivateIpAddresses"
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out
