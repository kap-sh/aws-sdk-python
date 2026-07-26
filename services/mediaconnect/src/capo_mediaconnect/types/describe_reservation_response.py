"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeReservationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.reservation


class DescribeReservationResponse(TypedDict, closed=True):
    reservation: NotRequired["capo_mediaconnect.types.reservation.Reservation"]
    """<p> A pricing agreement for a discounted rate for a specific outbound bandwidth that your MediaConnect account will use each month over a specific time period. The discounted rate in the reservation applies to outbound bandwidth for all flows from your account until your account reaches the amount of bandwidth in your reservation. If you use more outbound bandwidth than the agreed upon amount in a single month, the overage is charged at the on-demand rate. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReservationResponse) -> dict:
    out: dict = {}
    if "reservation" in value:
        import capo_mediaconnect.types.reservation

        out["reservation"] = capo_mediaconnect.types.reservation.serialize_json(
            value["reservation"]
        )
    return out


def deserialize_json(data: dict) -> DescribeReservationResponse:
    out: DescribeReservationResponse = {}  # type: ignore[typeddict-item]
    if "reservation" in data:
        import capo_mediaconnect.types.reservation

        out["reservation"] = capo_mediaconnect.types.reservation.deserialize_json(
            data["reservation"]
        )
    return out
