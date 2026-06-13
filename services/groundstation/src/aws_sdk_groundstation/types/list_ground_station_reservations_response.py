"""Generated from Smithy shape ``com.amazonaws.groundstation#ListGroundStationReservationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ground_station_reservation_list
    import aws_sdk_groundstation.types.pagination_token


class ListGroundStationReservationsResponse(TypedDict):
    reservation_list: "aws_sdk_groundstation.types.ground_station_reservation_list.GroundStationReservationList"
    """<p>List of ground station reservations.</p>"""
    next_token: NotRequired[
        "aws_sdk_groundstation.types.pagination_token.PaginationToken"
    ]
    """<p>Next token to be used in a subsequent <code>ListGroundStationReservations</code> call to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroundStationReservationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.ground_station_reservation_list

    out["reservationList"] = (
        aws_sdk_groundstation.types.ground_station_reservation_list.serialize_json(
            value["reservation_list"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroundStationReservationsResponse:
    out: ListGroundStationReservationsResponse = {}  # type: ignore[typeddict-item]
    if "reservationList" in data:
        import aws_sdk_groundstation.types.ground_station_reservation_list

        out["reservation_list"] = (
            aws_sdk_groundstation.types.ground_station_reservation_list.deserialize_json(
                data["reservationList"]
            )
        )
    else:
        raise DeserializationError(
            "ListGroundStationReservationsResponse.reservation_list required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
