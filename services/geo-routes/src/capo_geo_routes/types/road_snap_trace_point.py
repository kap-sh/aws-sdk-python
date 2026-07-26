"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapTracePoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.heading
    import capo_geo_routes.types.position
    import capo_geo_routes.types.speed_kilometers_per_hour
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RoadSnapTracePoint(TypedDict, closed=True):
    heading: "capo_geo_routes.types.heading.Heading"
    """<p>GPS Heading at the position.</p>"""
    position: "capo_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    speed: "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    """<p>Speed at the specified trace point .</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    timestamp: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Timestamp of the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapTracePoint) -> dict:
    out: dict = {}
    out["Heading"] = value.get("heading", 0)
    import capo_geo_routes.types.position

    out["Position"] = capo_geo_routes.types.position.serialize_json(value["position"])
    out["Speed"] = value.get("speed", 0)
    if "timestamp" in value:
        out["Timestamp"] = value["timestamp"]
    return out


def deserialize_json(data: dict) -> RoadSnapTracePoint:
    out: RoadSnapTracePoint = {}  # type: ignore[typeddict-item]
    if "Heading" in data:
        out["heading"] = data["Heading"]
    else:
        out["heading"] = 0
    if "Position" in data:
        import capo_geo_routes.types.position

        out["position"] = capo_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RoadSnapTracePoint.position required")
    if "Speed" in data:
        out["speed"] = data["Speed"]
    else:
        out["speed"] = 0
    if "Timestamp" in data:
        out["timestamp"] = data["Timestamp"]
    return out
