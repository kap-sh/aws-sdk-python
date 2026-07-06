"""Generated from Smithy shape ``com.amazonaws.controltower#DeleteLandingZoneInput``."""

from typing_extensions import TypedDict

from aws_sdk_controltower.errors import DeserializationError


class DeleteLandingZoneInput(TypedDict, closed=True):
    landing_zone_identifier: "str"
    """<p>The unique identifier of the landing zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLandingZoneInput) -> dict:
    out: dict = {}
    out["landingZoneIdentifier"] = value["landing_zone_identifier"]
    return out


def deserialize_json(data: dict) -> DeleteLandingZoneInput:
    out: DeleteLandingZoneInput = {}  # type: ignore[typeddict-item]
    if "landingZoneIdentifier" in data:
        out["landing_zone_identifier"] = data["landingZoneIdentifier"]
    else:
        raise DeserializationError(
            "DeleteLandingZoneInput.landing_zone_identifier required"
        )
    return out
