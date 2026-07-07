"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiTravelOnlySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds


class RouteTaxiTravelOnlySummary(TypedDict, closed=True):
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the travel portion of the taxi leg.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiTravelOnlySummary) -> dict:
    out: dict = {}
    out["Duration"] = value["duration"]
    return out


def deserialize_json(data: dict) -> RouteTaxiTravelOnlySummary:
    out: RouteTaxiTravelOnlySummary = {}  # type: ignore[typeddict-item]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        raise DeserializationError("RouteTaxiTravelOnlySummary.duration required")
    return out
