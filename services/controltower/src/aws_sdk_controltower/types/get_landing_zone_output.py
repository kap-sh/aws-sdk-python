"""Generated from Smithy shape ``com.amazonaws.controltower#GetLandingZoneOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.landing_zone_detail


class GetLandingZoneOutput(TypedDict):
    landing_zone: "aws_sdk_controltower.types.landing_zone_detail.LandingZoneDetail"
    """<p>Information about the landing zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLandingZoneOutput) -> dict:
    out: dict = {}
    import aws_sdk_controltower.types.landing_zone_detail

    out["landingZone"] = aws_sdk_controltower.types.landing_zone_detail.serialize_json(
        value["landing_zone"]
    )
    return out


def deserialize_json(data: dict) -> GetLandingZoneOutput:
    out: GetLandingZoneOutput = {}  # type: ignore[typeddict-item]
    if "landingZone" in data:
        import aws_sdk_controltower.types.landing_zone_detail

        out["landing_zone"] = (
            aws_sdk_controltower.types.landing_zone_detail.deserialize_json(
                data["landingZone"]
            )
        )
    else:
        raise DeserializationError("GetLandingZoneOutput.landing_zone required")
    return out
