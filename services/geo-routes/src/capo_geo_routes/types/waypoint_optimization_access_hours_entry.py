"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationAccessHoursEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.day_of_week
    import capo_geo_routes.types.time_of_day


class WaypointOptimizationAccessHoursEntry(TypedDict, closed=True):
    day_of_week: "capo_geo_routes.types.day_of_week.DayOfWeek"
    """<p>Day of the week.</p>"""
    time_of_day: "capo_geo_routes.types.time_of_day.TimeOfDay"
    """<p>Time of the day.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationAccessHoursEntry) -> dict:
    out: dict = {}
    import capo_geo_routes.types.day_of_week

    out["DayOfWeek"] = capo_geo_routes.types.day_of_week.serialize_json(
        value["day_of_week"]
    )
    out["TimeOfDay"] = value["time_of_day"]
    return out


def deserialize_json(data: dict) -> WaypointOptimizationAccessHoursEntry:
    out: WaypointOptimizationAccessHoursEntry = {}  # type: ignore[typeddict-item]
    if "DayOfWeek" in data:
        import capo_geo_routes.types.day_of_week

        out["day_of_week"] = capo_geo_routes.types.day_of_week.deserialize_json(
            data["DayOfWeek"]
        )
    else:
        raise DeserializationError(
            "WaypointOptimizationAccessHoursEntry.day_of_week required"
        )
    if "TimeOfDay" in data:
        out["time_of_day"] = data["TimeOfDay"]
    else:
        raise DeserializationError(
            "WaypointOptimizationAccessHoursEntry.time_of_day required"
        )
    return out
