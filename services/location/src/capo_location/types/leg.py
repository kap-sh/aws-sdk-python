"""Generated from Smithy shape ``com.amazonaws.location#Leg``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.leg_geometry
    import capo_location.types.position
    import capo_location.types.sensitive_double
    import capo_location.types.step_list


class Leg(TypedDict, closed=True):
    start_position: "capo_location.types.position.Position"
    r"""<p>The starting position of the leg. Follows the format <code>[longitude,latitude]</code>.</p> <note> <p>If the <code>StartPosition</code> isn't located on a road, it's <a href=\"https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html\">snapped to a nearby road</a>. </p> </note>"""
    end_position: "capo_location.types.position.Position"
    r"""<p>The terminating position of the leg. Follows the format <code>[longitude,latitude]</code>.</p> <note> <p>If the <code>EndPosition</code> isn't located on a road, it's <a href=\"https://docs.aws.amazon.com/location/previous/developerguide/nap-to-nearby-road.html\">snapped to a nearby road</a>. </p> </note>"""
    distance: "capo_location.types.sensitive_double.SensitiveDouble"
    """<p>The distance between the leg's <code>StartPosition</code> and <code>EndPosition</code> along a calculated route. </p> <ul> <li> <p>The default measurement is <code>Kilometers</code> unless the request specifies a <code>DistanceUnit</code> of <code>Miles</code>.</p> </li> </ul>"""
    duration_seconds: "capo_location.types.sensitive_double.SensitiveDouble"
    """<p>The estimated travel time between the leg's <code>StartPosition</code> and <code>EndPosition</code>. The travel mode and departure time that you specify in the request determines the calculated time.</p>"""
    geometry: NotRequired["capo_location.types.leg_geometry.LegGeometry"]
    """<p>Contains the calculated route's path as a linestring geometry.</p>"""
    steps: "capo_location.types.step_list.StepList"
    """<p>Contains a list of steps, which represent subsections of a leg. Each step provides instructions for how to move to the next step in the leg such as the step's start position, end position, travel distance, travel duration, and geometry offset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Leg) -> dict:
    out: dict = {}
    import capo_location.types.position

    out["StartPosition"] = capo_location.types.position.serialize_json(
        value["start_position"]
    )
    import capo_location.types.position

    out["EndPosition"] = capo_location.types.position.serialize_json(
        value["end_position"]
    )
    out["Distance"] = value["distance"]
    out["DurationSeconds"] = value["duration_seconds"]
    if "geometry" in value:
        import capo_location.types.leg_geometry

        out["Geometry"] = capo_location.types.leg_geometry.serialize_json(
            value["geometry"]
        )
    import capo_location.types.step_list

    out["Steps"] = capo_location.types.step_list.serialize_json(value["steps"])
    return out


def deserialize_json(data: dict) -> Leg:
    out: Leg = {}  # type: ignore[typeddict-item]
    if "StartPosition" in data:
        import capo_location.types.position

        out["start_position"] = capo_location.types.position.deserialize_json(
            data["StartPosition"]
        )
    else:
        raise DeserializationError("Leg.start_position required")
    if "EndPosition" in data:
        import capo_location.types.position

        out["end_position"] = capo_location.types.position.deserialize_json(
            data["EndPosition"]
        )
    else:
        raise DeserializationError("Leg.end_position required")
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        raise DeserializationError("Leg.distance required")
    if "DurationSeconds" in data:
        out["duration_seconds"] = data["DurationSeconds"]
    else:
        raise DeserializationError("Leg.duration_seconds required")
    if "Geometry" in data:
        import capo_location.types.leg_geometry

        out["geometry"] = capo_location.types.leg_geometry.deserialize_json(
            data["Geometry"]
        )
    if "Steps" in data:
        import capo_location.types.step_list

        out["steps"] = capo_location.types.step_list.deserialize_json(data["Steps"])
    else:
        raise DeserializationError("Leg.steps required")
    return out
