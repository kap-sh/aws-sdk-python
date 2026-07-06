"""Generated from Smithy shape ``com.amazonaws.controltower#ListLandingZonesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controltower.types.landing_zone_summaries


class ListLandingZonesOutput(TypedDict, closed=True):
    landing_zones: (
        "aws_sdk_controltower.types.landing_zone_summaries.LandingZoneSummaries"
    )
    """<p>The ARN of the landing zone.</p>"""
    next_token: NotRequired["str"]
    """<p>Retrieves the next page of results. If the string is empty, the response is the end of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLandingZonesOutput) -> dict:
    out: dict = {}
    import aws_sdk_controltower.types.landing_zone_summaries

    out["landingZones"] = (
        aws_sdk_controltower.types.landing_zone_summaries.serialize_json(
            value["landing_zones"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLandingZonesOutput:
    out: ListLandingZonesOutput = {}  # type: ignore[typeddict-item]
    if "landingZones" in data:
        import aws_sdk_controltower.types.landing_zone_summaries

        out["landing_zones"] = (
            aws_sdk_controltower.types.landing_zone_summaries.deserialize_json(
                data["landingZones"]
            )
        )
    else:
        raise DeserializationError("ListLandingZonesOutput.landing_zones required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
