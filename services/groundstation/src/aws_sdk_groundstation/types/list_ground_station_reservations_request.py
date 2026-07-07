"""Generated from Smithy shape ``com.amazonaws.groundstation#ListGroundStationReservationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_groundstation.types.ground_station_name
    import aws_sdk_groundstation.types.pagination_max_results
    import aws_sdk_groundstation.types.pagination_token
    import aws_sdk_groundstation.types.reservation_type_filter_list


class ListGroundStationReservationsRequest(TypedDict, closed=True):
    ground_station_id: (
        "aws_sdk_groundstation.types.ground_station_name.GroundStationName"
    )
    """<p>ID of a ground station.</p>"""
    start_time: "datetime.datetime"
    """<p>Start time of the reservation window in UTC.</p>"""
    end_time: "datetime.datetime"
    """<p>End time of the reservation window in UTC.</p>"""
    reservation_types: NotRequired[
        "aws_sdk_groundstation.types.reservation_type_filter_list.ReservationTypeFilterList"
    ]
    """<p>Types of reservations to filter by.</p>"""
    max_results: NotRequired[
        "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Maximum number of ground station reservations returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_groundstation.types.pagination_token.PaginationToken"
    ]
    """<p>Next token returned in the request of a previous <code>ListGroundStationReservations</code> call. Used to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroundStationReservationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListGroundStationReservationsRequest:
    out: ListGroundStationReservationsRequest = {}  # type: ignore[typeddict-item]
    return out
