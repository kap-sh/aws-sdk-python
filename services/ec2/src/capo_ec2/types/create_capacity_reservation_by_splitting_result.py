"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationBySplittingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation
    import capo_ec2.types.integer


class CreateCapacityReservationBySplittingResult(TypedDict, closed=True):
    source_capacity_reservation: NotRequired[
        "capo_ec2.types.capacity_reservation.CapacityReservation"
    ]
    """<p> Information about the source Capacity Reservation. </p>"""
    destination_capacity_reservation: NotRequired[
        "capo_ec2.types.capacity_reservation.CapacityReservation"
    ]
    """<p> Information about the destination Capacity Reservation. </p>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p> The number of instances in the new Capacity Reservation. The number of instances in the source Capacity Reservation was reduced by this amount. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCapacityReservationBySplittingResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_capacity_reservation" in value:
        import capo_ec2.types.capacity_reservation

        capo_ec2.types.capacity_reservation.serialize_ec2_query(
            value["source_capacity_reservation"],
            pairs,
            f"{key_prefix}SourceCapacityReservation",
        )
    if "destination_capacity_reservation" in value:
        import capo_ec2.types.capacity_reservation

        capo_ec2.types.capacity_reservation.serialize_ec2_query(
            value["destination_capacity_reservation"],
            pairs,
            f"{key_prefix}DestinationCapacityReservation",
        )
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))


def deserialize_ec2_query(el: Element) -> CreateCapacityReservationBySplittingResult:
    out: CreateCapacityReservationBySplittingResult = {}  # type: ignore[typeddict-item]
    child_source_capacity_reservation = el.find("SourceCapacityReservation")
    if child_source_capacity_reservation is not None:
        import capo_ec2.types.capacity_reservation

        out["source_capacity_reservation"] = (
            capo_ec2.types.capacity_reservation.deserialize_ec2_query(
                child_source_capacity_reservation
            )
        )
    child_destination_capacity_reservation = el.find("DestinationCapacityReservation")
    if child_destination_capacity_reservation is not None:
        import capo_ec2.types.capacity_reservation

        out["destination_capacity_reservation"] = (
            capo_ec2.types.capacity_reservation.deserialize_ec2_query(
                child_destination_capacity_reservation
            )
        )
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    return out
