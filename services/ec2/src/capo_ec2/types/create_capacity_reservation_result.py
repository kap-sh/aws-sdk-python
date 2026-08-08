"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_reservation


class CreateCapacityReservationResult(TypedDict, closed=True):
    capacity_reservation: NotRequired[
        "capo_ec2.types.capacity_reservation.CapacityReservation"
    ]
    """<p>Information about the Capacity Reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCapacityReservationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation" in value:
        import capo_ec2.types.capacity_reservation

        capo_ec2.types.capacity_reservation.serialize_ec2_query(
            value["capacity_reservation"], pairs, f"{key_prefix}CapacityReservation"
        )


def deserialize_ec2_query(el: Element) -> CreateCapacityReservationResult:
    out: CreateCapacityReservationResult = {}  # type: ignore[typeddict-item]
    child_capacity_reservation = el.find("capacityReservation")
    if child_capacity_reservation is not None:
        import capo_ec2.types.capacity_reservation

        out["capacity_reservation"] = (
            capo_ec2.types.capacity_reservation.deserialize_ec2_query(
                child_capacity_reservation
            )
        )
    return out
