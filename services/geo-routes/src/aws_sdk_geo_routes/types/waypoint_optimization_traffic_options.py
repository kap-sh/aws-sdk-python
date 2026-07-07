"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationTrafficOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.traffic_usage


class WaypointOptimizationTrafficOptions(TypedDict, closed=True):
    usage: NotRequired["aws_sdk_geo_routes.types.traffic_usage.TrafficUsage"]
    """<p>Determines if traffic should be used or ignored while calculating the route.</p> <p>Default value: <code>UseTrafficData</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationTrafficOptions) -> dict:
    out: dict = {}
    if "usage" in value:
        import aws_sdk_geo_routes.types.traffic_usage

        out["Usage"] = aws_sdk_geo_routes.types.traffic_usage.serialize_json(
            value["usage"]
        )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationTrafficOptions:
    out: WaypointOptimizationTrafficOptions = {}  # type: ignore[typeddict-item]
    if "Usage" in data:
        import aws_sdk_geo_routes.types.traffic_usage

        out["usage"] = aws_sdk_geo_routes.types.traffic_usage.deserialize_json(
            data["Usage"]
        )
    return out
