"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PurchaseOfferingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.reservation


class PurchaseOfferingResponse(TypedDict, closed=True):
    reservation: NotRequired["capo_mediaconnect.types.reservation.Reservation"]
    """<p>The details of the reservation that you just created when you purchased the offering. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOfferingResponse) -> dict:
    out: dict = {}
    if "reservation" in value:
        import capo_mediaconnect.types.reservation

        out["reservation"] = capo_mediaconnect.types.reservation.serialize_json(
            value["reservation"]
        )
    return out


def deserialize_json(data: dict) -> PurchaseOfferingResponse:
    out: PurchaseOfferingResponse = {}  # type: ignore[typeddict-item]
    if "reservation" in data:
        import capo_mediaconnect.types.reservation

        out["reservation"] = capo_mediaconnect.types.reservation.deserialize_json(
            data["reservation"]
        )
    return out
