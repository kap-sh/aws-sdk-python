"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationRestCycles``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_rest_cycle_durations


class WaypointOptimizationRestCycles(TypedDict, closed=True):
    long_cycle: "capo_geo_routes.types.waypoint_optimization_rest_cycle_durations.WaypointOptimizationRestCycleDurations"
    """<p>Long cycle for a driver work-rest schedule.</p>"""
    short_cycle: "capo_geo_routes.types.waypoint_optimization_rest_cycle_durations.WaypointOptimizationRestCycleDurations"
    """<p>Short cycle for a driver work-rest schedule</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationRestCycles) -> dict:
    out: dict = {}
    import capo_geo_routes.types.waypoint_optimization_rest_cycle_durations

    out["LongCycle"] = (
        capo_geo_routes.types.waypoint_optimization_rest_cycle_durations.serialize_json(
            value["long_cycle"]
        )
    )
    import capo_geo_routes.types.waypoint_optimization_rest_cycle_durations

    out["ShortCycle"] = (
        capo_geo_routes.types.waypoint_optimization_rest_cycle_durations.serialize_json(
            value["short_cycle"]
        )
    )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationRestCycles:
    out: WaypointOptimizationRestCycles = {}  # type: ignore[typeddict-item]
    if "LongCycle" in data:
        import capo_geo_routes.types.waypoint_optimization_rest_cycle_durations

        out["long_cycle"] = (
            capo_geo_routes.types.waypoint_optimization_rest_cycle_durations.deserialize_json(
                data["LongCycle"]
            )
        )
    else:
        raise DeserializationError("WaypointOptimizationRestCycles.long_cycle required")
    if "ShortCycle" in data:
        import capo_geo_routes.types.waypoint_optimization_rest_cycle_durations

        out["short_cycle"] = (
            capo_geo_routes.types.waypoint_optimization_rest_cycle_durations.deserialize_json(
                data["ShortCycle"]
            )
        )
    else:
        raise DeserializationError(
            "WaypointOptimizationRestCycles.short_cycle required"
        )
    return out
