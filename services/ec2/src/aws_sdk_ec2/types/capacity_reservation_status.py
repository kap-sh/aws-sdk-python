"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation_id
    import aws_sdk_ec2.types.integer


class CapacityReservationStatus(TypedDict, closed=True):
    capacity_reservation_id: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation_id.CapacityReservationId"
    ]
    """<p>The ID of the Capacity Reservation.</p>"""
    total_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The combined amount of <code>Available</code> and <code>Unavailable</code> capacity in the Capacity Reservation.</p>"""
    total_available_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The remaining capacity. Indicates the amount of resources that can be launched into the Capacity Reservation.</p>"""
    total_unavailable_capacity: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The used capacity. Indicates that the capacity is in use by resources that are running in the Capacity Reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_reservation_id" in value:
        pairs.append(
            (f"{prefix}.CapacityReservationId", str(value["capacity_reservation_id"]))
        )
    if "total_capacity" in value:
        pairs.append((f"{prefix}.TotalCapacity", str(value["total_capacity"])))
    if "total_available_capacity" in value:
        pairs.append(
            (f"{prefix}.TotalAvailableCapacity", str(value["total_available_capacity"]))
        )
    if "total_unavailable_capacity" in value:
        pairs.append(
            (
                f"{prefix}.TotalUnavailableCapacity",
                str(value["total_unavailable_capacity"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CapacityReservationStatus:
    out: CapacityReservationStatus = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("CapacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_total_capacity = el.find("TotalCapacity")
    if child_total_capacity is not None:
        out["total_capacity"] = int(child_total_capacity.text or "")
    child_total_available_capacity = el.find("TotalAvailableCapacity")
    if child_total_available_capacity is not None:
        out["total_available_capacity"] = int(child_total_available_capacity.text or "")
    child_total_unavailable_capacity = el.find("TotalUnavailableCapacity")
    if child_total_unavailable_capacity is not None:
        out["total_unavailable_capacity"] = int(
            child_total_unavailable_capacity.text or ""
        )
    return out
