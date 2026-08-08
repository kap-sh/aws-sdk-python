"""Generated from Smithy shape ``com.amazonaws.ec2#NatGatewayAddress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.availability_zone_name
    import capo_ec2.types.boolean
    import capo_ec2.types.nat_gateway_address_status
    import capo_ec2.types.string


class NatGatewayAddress(TypedDict, closed=True):
    allocation_id: NotRequired["capo_ec2.types.string.String"]
    """<p>[Public NAT gateway only] The allocation ID of the Elastic IP address that's associated with the NAT gateway.</p>"""
    network_interface_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network interface associated with the NAT gateway.</p>"""
    private_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>The private IP address associated with the NAT gateway.</p>"""
    public_ip: NotRequired["capo_ec2.types.string.String"]
    """<p>[Public NAT gateway only] The Elastic IP address associated with the NAT gateway.</p>"""
    association_id: NotRequired["capo_ec2.types.string.String"]
    """<p>[Public NAT gateway only] The association ID of the Elastic IP address that's associated with the NAT gateway.</p>"""
    is_primary: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Defines if the IP address is the primary address.</p>"""
    failure_message: NotRequired["capo_ec2.types.string.String"]
    """<p>The address failure message.</p>"""
    status: NotRequired[
        "capo_ec2.types.nat_gateway_address_status.NatGatewayAddressStatus"
    ]
    """<p>The address status.</p>"""
    availability_zone: NotRequired[
        "capo_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone where this Elastic IP address (EIP) is being used to handle outbound NAT traffic.</p>"""
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone where this Elastic IP address (EIP) is being used to handle outbound NAT traffic. Use this instead of AvailabilityZone for consistent identification of AZs across Amazon Web Services Regions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NatGatewayAddress, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allocation_id" in value:
        pairs.append((f"{key_prefix}AllocationId", str(value["allocation_id"])))
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "private_ip" in value:
        pairs.append((f"{key_prefix}PrivateIp", str(value["private_ip"])))
    if "public_ip" in value:
        pairs.append((f"{key_prefix}PublicIp", str(value["public_ip"])))
    if "association_id" in value:
        pairs.append((f"{key_prefix}AssociationId", str(value["association_id"])))
    if "is_primary" in value:
        pairs.append(
            (f"{key_prefix}IsPrimary", "true" if value["is_primary"] else "false")
        )
    if "failure_message" in value:
        pairs.append((f"{key_prefix}FailureMessage", str(value["failure_message"])))
    if "status" in value:
        import capo_ec2.types.nat_gateway_address_status

        capo_ec2.types.nat_gateway_address_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> NatGatewayAddress:
    out: NatGatewayAddress = {}  # type: ignore[typeddict-item]
    child_allocation_id = el.find("allocationId")
    if child_allocation_id is not None:
        out["allocation_id"] = str(child_allocation_id.text or "")
    child_network_interface_id = el.find("networkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_private_ip = el.find("privateIp")
    if child_private_ip is not None:
        out["private_ip"] = str(child_private_ip.text or "")
    child_public_ip = el.find("publicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    child_association_id = el.find("associationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    child_is_primary = el.find("isPrimary")
    if child_is_primary is not None:
        out["is_primary"] = (child_is_primary.text or "").lower() == "true"
    child_failure_message = el.find("failureMessage")
    if child_failure_message is not None:
        out["failure_message"] = str(child_failure_message.text or "")
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.nat_gateway_address_status

        out["status"] = capo_ec2.types.nat_gateway_address_status.deserialize_ec2_query(
            child_status
        )
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out
