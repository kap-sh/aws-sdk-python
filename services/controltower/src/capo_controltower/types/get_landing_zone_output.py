"""Generated from Smithy shape ``com.amazonaws.controltower#GetLandingZoneOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controltower.types.landing_zone_detail


class GetLandingZoneOutput(TypedDict, closed=True):
    landing_zone: "capo_controltower.types.landing_zone_detail.LandingZoneDetail"
    """<p>Information about the landing zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLandingZoneOutput) -> dict:
    out: dict = {}
    import capo_controltower.types.landing_zone_detail

    out["landingZone"] = capo_controltower.types.landing_zone_detail.serialize_json(
        value["landing_zone"]
    )
    return out


def deserialize_json(data: dict) -> GetLandingZoneOutput:
    out: GetLandingZoneOutput = {}  # type: ignore[typeddict-item]
    if "landingZone" in data:
        import capo_controltower.types.landing_zone_detail

        out["landing_zone"] = (
            capo_controltower.types.landing_zone_detail.deserialize_json(
                data["landingZone"]
            )
        )
    else:
        raise DeserializationError("GetLandingZoneOutput.landing_zone required")
    return out
