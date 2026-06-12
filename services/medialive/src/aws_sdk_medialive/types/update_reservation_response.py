"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateReservationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.reservation


class UpdateReservationResponse(TypedDict):
    reservation: NotRequired["aws_sdk_medialive.types.reservation.Reservation"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReservationResponse) -> dict:
    out: dict = {}
    if "reservation" in value:
        import aws_sdk_medialive.types.reservation

        out["reservation"] = aws_sdk_medialive.types.reservation.serialize_json(
            value["reservation"]
        )
    return out


def deserialize_json(data: dict) -> UpdateReservationResponse:
    out: UpdateReservationResponse = {}  # type: ignore[typeddict-item]
    if "reservation" in data:
        import aws_sdk_medialive.types.reservation

        out["reservation"] = aws_sdk_medialive.types.reservation.deserialize_json(
            data["reservation"]
        )
    return out
