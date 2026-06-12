"""Generated from Smithy shape ``com.amazonaws.medialive#PurchaseOfferingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.reservation


class PurchaseOfferingResponse(TypedDict):
    reservation: NotRequired["aws_sdk_medialive.types.reservation.Reservation"]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOfferingResponse) -> dict:
    out: dict = {}
    if "reservation" in value:
        import aws_sdk_medialive.types.reservation

        out["reservation"] = aws_sdk_medialive.types.reservation.serialize_json(
            value["reservation"]
        )
    return out


def deserialize_json(data: dict) -> PurchaseOfferingResponse:
    out: PurchaseOfferingResponse = {}  # type: ignore[typeddict-item]
    if "reservation" in data:
        import aws_sdk_medialive.types.reservation

        out["reservation"] = aws_sdk_medialive.types.reservation.deserialize_json(
            data["reservation"]
        )
    return out
