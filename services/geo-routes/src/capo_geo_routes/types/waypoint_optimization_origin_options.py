"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationOriginOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_id


class WaypointOptimizationOriginOptions(TypedDict, closed=True):
    id: NotRequired["capo_geo_routes.types.waypoint_id.WaypointId"]
    """<p>The Origin Id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationOriginOptions) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> WaypointOptimizationOriginOptions:
    out: WaypointOptimizationOriginOptions = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
