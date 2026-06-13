"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeReservationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.reservation


class DescribeReservationResponse(TypedDict):
    reservation: NotRequired["aws_sdk_mediaconnect.types.reservation.Reservation"]
    """<p> A pricing agreement for a discounted rate for a specific outbound bandwidth that your MediaConnect account will use each month over a specific time period. The discounted rate in the reservation applies to outbound bandwidth for all flows from your account until your account reaches the amount of bandwidth in your reservation. If you use more outbound bandwidth than the agreed upon amount in a single month, the overage is charged at the on-demand rate. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReservationResponse) -> dict:
    out: dict = {}
    if "reservation" in value:
        import aws_sdk_mediaconnect.types.reservation

        out["reservation"] = aws_sdk_mediaconnect.types.reservation.serialize_json(
            value["reservation"]
        )
    return out


def deserialize_json(data: dict) -> DescribeReservationResponse:
    out: DescribeReservationResponse = {}  # type: ignore[typeddict-item]
    if "reservation" in data:
        import aws_sdk_mediaconnect.types.reservation

        out["reservation"] = aws_sdk_mediaconnect.types.reservation.deserialize_json(
            data["reservation"]
        )
    return out
