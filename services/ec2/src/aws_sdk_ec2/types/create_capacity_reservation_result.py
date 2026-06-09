"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_reservation


class CreateCapacityReservationResult(TypedDict):
    capacity_reservation: NotRequired[
        "aws_sdk_ec2.types.capacity_reservation.CapacityReservation"
    ]
    """<p>Information about the Capacity Reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCapacityReservationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "capacity_reservation" in value:
        import aws_sdk_ec2.types.capacity_reservation

        aws_sdk_ec2.types.capacity_reservation.serialize_ec2_query(
            value["capacity_reservation"], pairs, f"{prefix}.CapacityReservation"
        )


def deserialize_ec2_query(el: Element) -> CreateCapacityReservationResult:
    out: CreateCapacityReservationResult = {}  # type: ignore[typeddict-item]
    child_capacity_reservation = el.find("CapacityReservation")
    if child_capacity_reservation is not None:
        import aws_sdk_ec2.types.capacity_reservation

        out["capacity_reservation"] = (
            aws_sdk_ec2.types.capacity_reservation.deserialize_ec2_query(
                child_capacity_reservation
            )
        )
    return out
