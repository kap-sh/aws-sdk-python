"""Generated from Smithy shape ``com.amazonaws.groundstation#ListAntennasRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.ground_station_name
    import aws_sdk_groundstation.types.pagination_max_results
    import aws_sdk_groundstation.types.pagination_token


class ListAntennasRequest(TypedDict):
    ground_station_id: (
        "aws_sdk_groundstation.types.ground_station_name.GroundStationName"
    )
    """<p>ID of a ground station.</p>"""
    max_results: NotRequired[
        "aws_sdk_groundstation.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>Maximum number of antennas returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_groundstation.types.pagination_token.PaginationToken"
    ]
    """<p>Next token returned in the request of a previous <code>ListAntennas</code> call. Used to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAntennasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAntennasRequest:
    out: ListAntennasRequest = {}  # type: ignore[typeddict-item]
    return out
