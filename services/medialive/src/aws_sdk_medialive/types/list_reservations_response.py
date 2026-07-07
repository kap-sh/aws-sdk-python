"""Generated from Smithy shape ``com.amazonaws.medialive#ListReservationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_reservation
    import aws_sdk_medialive.types.__string


class ListReservationsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Token to retrieve the next page of results"""
    reservations: NotRequired[
        "aws_sdk_medialive.types.__list_of_reservation.__listOfReservation"
    ]
    """List of reservations"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReservationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "reservations" in value:
        import aws_sdk_medialive.types.__list_of_reservation

        out["reservations"] = (
            aws_sdk_medialive.types.__list_of_reservation.serialize_json(
                value["reservations"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListReservationsResponse:
    out: ListReservationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "reservations" in data:
        import aws_sdk_medialive.types.__list_of_reservation

        out["reservations"] = (
            aws_sdk_medialive.types.__list_of_reservation.deserialize_json(
                data["reservations"]
            )
        )
    return out
