"""Generated from Smithy shape ``com.amazonaws.controltower#GetLandingZoneInput``."""

from typing import TypedDict

from aws_sdk_controltower.errors import DeserializationError


class GetLandingZoneInput(TypedDict):
    landing_zone_identifier: "str"
    """<p>The unique identifier of the landing zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLandingZoneInput) -> dict:
    out: dict = {}
    out["landingZoneIdentifier"] = value["landing_zone_identifier"]
    return out


def deserialize_json(data: dict) -> GetLandingZoneInput:
    out: GetLandingZoneInput = {}  # type: ignore[typeddict-item]
    if "landingZoneIdentifier" in data:
        out["landing_zone_identifier"] = data["landingZoneIdentifier"]
    else:
        raise DeserializationError(
            "GetLandingZoneInput.landing_zone_identifier required"
        )
    return out
