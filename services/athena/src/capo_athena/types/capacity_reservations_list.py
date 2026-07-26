"""Generated from Smithy shape ``com.amazonaws.athena#CapacityReservationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.capacity_reservation

CapacityReservationsList: TypeAlias = list[
    "capo_athena.types.capacity_reservation.CapacityReservation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityReservationsList) -> list:
    import capo_athena.types.capacity_reservation

    out: list = []
    for item in value:
        out.append(capo_athena.types.capacity_reservation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CapacityReservationsList:
    import capo_athena.types.capacity_reservation

    out: CapacityReservationsList = []
    for item in data:
        out.append(
            capo_athena.types.capacity_reservation.deserialize_aws_json_1_1(item)
        )
    return out
