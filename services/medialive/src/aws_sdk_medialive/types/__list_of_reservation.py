"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfReservation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.reservation

__listOfReservation: TypeAlias = list["aws_sdk_medialive.types.reservation.Reservation"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfReservation) -> list:
    import aws_sdk_medialive.types.reservation

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.reservation.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfReservation:
    import aws_sdk_medialive.types.reservation

    out: __listOfReservation = []
    for item in data:
        out.append(aws_sdk_medialive.types.reservation.deserialize_json(item))
    return out
