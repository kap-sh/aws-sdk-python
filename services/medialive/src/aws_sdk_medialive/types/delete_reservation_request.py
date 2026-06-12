"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteReservationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DeleteReservationRequest(TypedDict):
    reservation_id: "aws_sdk_medialive.types.__string.__string"
    """Unique reservation ID, e.g. '1234567'"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReservationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteReservationRequest:
    out: DeleteReservationRequest = {}  # type: ignore[typeddict-item]
    return out
