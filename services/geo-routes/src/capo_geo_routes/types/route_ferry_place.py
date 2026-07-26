"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryPlace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.position23
    import capo_geo_routes.types.sensitive_integer
    import capo_geo_routes.types.sensitive_string


class RouteFerryPlace(TypedDict, closed=True):
    name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The name of the place.</p>"""
    original_position: NotRequired["capo_geo_routes.types.position23.Position23"]
    """<p>Position provided in the request.</p>"""
    position: "capo_geo_routes.types.position23.Position23"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    waypoint_index: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Index of the waypoint in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryPlace) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "original_position" in value:
        import capo_geo_routes.types.position23

        out["OriginalPosition"] = capo_geo_routes.types.position23.serialize_json(
            value["original_position"]
        )
    import capo_geo_routes.types.position23

    out["Position"] = capo_geo_routes.types.position23.serialize_json(value["position"])
    if "waypoint_index" in value:
        out["WaypointIndex"] = value["waypoint_index"]
    return out


def deserialize_json(data: dict) -> RouteFerryPlace:
    out: RouteFerryPlace = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "OriginalPosition" in data:
        import capo_geo_routes.types.position23

        out["original_position"] = capo_geo_routes.types.position23.deserialize_json(
            data["OriginalPosition"]
        )
    if "Position" in data:
        import capo_geo_routes.types.position23

        out["position"] = capo_geo_routes.types.position23.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RouteFerryPlace.position required")
    if "WaypointIndex" in data:
        out["waypoint_index"] = data["WaypointIndex"]
    return out
