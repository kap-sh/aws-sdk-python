"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.renewal_settings


class UpdateReservationRequest(TypedDict, closed=True):
    name: NotRequired["capo_medialive.types.__string.__string"]
    """Name of the reservation"""
    renewal_settings: NotRequired[
        "capo_medialive.types.renewal_settings.RenewalSettings"
    ]
    """Renewal settings for the reservation"""
    reservation_id: "capo_medialive.types.__string.__string"
    """Unique reservation ID, e.g. '1234567'"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReservationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "renewal_settings" in value:
        import capo_medialive.types.renewal_settings

        out["renewalSettings"] = capo_medialive.types.renewal_settings.serialize_json(
            value["renewal_settings"]
        )
    return out


def deserialize_json(data: dict) -> UpdateReservationRequest:
    out: UpdateReservationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "renewalSettings" in data:
        import capo_medialive.types.renewal_settings

        out["renewal_settings"] = (
            capo_medialive.types.renewal_settings.deserialize_json(
                data["renewalSettings"]
            )
        )
    return out
