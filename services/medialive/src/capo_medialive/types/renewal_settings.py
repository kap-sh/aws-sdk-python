"""Generated from Smithy shape ``com.amazonaws.medialive#RenewalSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min1
    import capo_medialive.types.reservation_automatic_renewal


class RenewalSettings(TypedDict, closed=True):
    automatic_renewal: NotRequired[
        "capo_medialive.types.reservation_automatic_renewal.ReservationAutomaticRenewal"
    ]
    """Automatic renewal status for the reservation"""
    renewal_count: NotRequired["capo_medialive.types.__integer_min1.__integerMin1"]
    """Count for the reservation renewal"""


# --- restJson1 ser/de ---
def serialize_json(value: RenewalSettings) -> dict:
    out: dict = {}
    if "automatic_renewal" in value:
        import capo_medialive.types.reservation_automatic_renewal

        out["automaticRenewal"] = (
            capo_medialive.types.reservation_automatic_renewal.serialize_json(
                value["automatic_renewal"]
            )
        )
    if "renewal_count" in value:
        out["renewalCount"] = value["renewal_count"]
    return out


def deserialize_json(data: dict) -> RenewalSettings:
    out: RenewalSettings = {}  # type: ignore[typeddict-item]
    if "automaticRenewal" in data:
        import capo_medialive.types.reservation_automatic_renewal

        out["automatic_renewal"] = (
            capo_medialive.types.reservation_automatic_renewal.deserialize_json(
                data["automaticRenewal"]
            )
        )
    if "renewalCount" in data:
        out["renewal_count"] = data["renewalCount"]
    return out
