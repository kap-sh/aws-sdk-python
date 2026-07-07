"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.reservation_arn


class DescribeReservationRequest(TypedDict, closed=True):
    reservation_arn: "aws_sdk_mediaconnect.types.reservation_arn.ReservationArn"
    """<p>The Amazon Resource Name (ARN) of the offering. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReservationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeReservationRequest:
    out: DescribeReservationRequest = {}  # type: ignore[typeddict-item]
    return out
