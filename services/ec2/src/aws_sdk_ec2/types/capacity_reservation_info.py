"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.availability_zone_name
    import aws_sdk_ec2.types.capacity_reservation_tenancy
    import aws_sdk_ec2.types.string


class CapacityReservationInfo(TypedDict):
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type for the Capacity Reservation.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone for the Capacity Reservation.</p>"""
    tenancy: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_tenancy.CapacityReservationTenancy"
    ]
    """<p>The tenancy of the Capacity Reservation.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_type" in value:
        pairs.append((f"{prefix}.InstanceType", str(value["instance_type"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "tenancy" in value:
        import aws_sdk_ec2.types.capacity_reservation_tenancy

        aws_sdk_ec2.types.capacity_reservation_tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{prefix}.Tenancy"
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationInfo:
    out: CapacityReservationInfo = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_tenancy = el.find("Tenancy")
    if child_tenancy is not None:
        import aws_sdk_ec2.types.capacity_reservation_tenancy

        out["tenancy"] = (
            aws_sdk_ec2.types.capacity_reservation_tenancy.deserialize_ec2_query(
                child_tenancy
            )
        )
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out
