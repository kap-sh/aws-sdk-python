"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListReservationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_reservation


class ListReservationsResponse(TypedDict):
    next_token: NotRequired["str"]
    """<p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListReservations</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListReservations</code> request a second time and specify the <code>NextToken</code> value.</p>"""
    reservations: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_reservation.__listOfReservation"
    ]
    """<p> A list of all reservations that have been purchased by this account in the current Amazon Web Services Region. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReservationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "reservations" in value:
        import aws_sdk_mediaconnect.types.__list_of_reservation

        out["reservations"] = (
            aws_sdk_mediaconnect.types.__list_of_reservation.serialize_json(
                value["reservations"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListReservationsResponse:
    out: ListReservationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "reservations" in data:
        import aws_sdk_mediaconnect.types.__list_of_reservation

        out["reservations"] = (
            aws_sdk_mediaconnect.types.__list_of_reservation.deserialize_json(
                data["reservations"]
            )
        )
    return out
