"""Generated from Smithy shape ``com.amazonaws.mediaconnect#__listOfReservation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.reservation

__listOfReservation: TypeAlias = list["capo_mediaconnect.types.reservation.Reservation"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfReservation) -> list:
    import capo_mediaconnect.types.reservation

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.reservation.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfReservation:
    import capo_mediaconnect.types.reservation

    out: __listOfReservation = []
    for item in data:
        out.append(capo_mediaconnect.types.reservation.deserialize_json(item))
    return out
