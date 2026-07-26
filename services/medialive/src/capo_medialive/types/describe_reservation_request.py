"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DescribeReservationRequest(TypedDict, closed=True):
    reservation_id: "capo_medialive.types.__string.__string"
    """Unique reservation ID, e.g. '1234567'"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeReservationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeReservationRequest:
    out: DescribeReservationRequest = {}  # type: ignore[typeddict-item]
    return out
