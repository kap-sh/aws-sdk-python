"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianTravelOnlySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.duration_seconds


class RoutePedestrianTravelOnlySummary(TypedDict, closed=True):
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the step.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianTravelOnlySummary) -> dict:
    out: dict = {}
    out["Duration"] = value.get("duration", 0)
    return out


def deserialize_json(data: dict) -> RoutePedestrianTravelOnlySummary:
    out: RoutePedestrianTravelOnlySummary = {}  # type: ignore[typeddict-item]
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    return out
