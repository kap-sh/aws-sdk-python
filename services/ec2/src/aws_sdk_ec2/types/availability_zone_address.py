"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneAddress``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_id_list
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name


class AvailabilityZoneAddress(TypedDict):
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>For regional NAT gateways only: The Availability Zone where this specific NAT gateway configuration will be active. Each AZ in a regional NAT gateway has its own configuration to handle outbound NAT traffic from that AZ. </p> <p>A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>For regional NAT gateways only: The ID of the Availability Zone where this specific NAT gateway configuration will be active. Each AZ in a regional NAT gateway has its own configuration to handle outbound NAT traffic from that AZ. Use this instead of AvailabilityZone for consistent identification of AZs across Amazon Web Services Regions. </p> <p>A regional NAT gateway is a single NAT Gateway that works across multiple availability zones (AZs) in your VPC, providing redundancy, scalability and availability across all the AZs in a Region.</p>"""
    allocation_ids: NotRequired["aws_sdk_ec2.types.allocation_id_list.AllocationIdList"]
    """<p>The allocation IDs of the Elastic IP addresses (EIPs) to be used for handling outbound NAT traffic in this specific Availability Zone.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZoneAddress, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "allocation_ids" in value:
        import aws_sdk_ec2.types.allocation_id_list

        aws_sdk_ec2.types.allocation_id_list.serialize_ec2_query(
            value["allocation_ids"], pairs, f"{prefix}.AllocationIds"
        )


def deserialize_ec2_query(el: Element) -> AvailabilityZoneAddress:
    out: AvailabilityZoneAddress = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    if el.find("AllocationIds") is not None:
        import aws_sdk_ec2.types.allocation_id_list

        out["allocation_ids"] = (
            aws_sdk_ec2.types.allocation_id_list.deserialize_ec2_query(
                el, "AllocationIds"
            )
        )
    return out
