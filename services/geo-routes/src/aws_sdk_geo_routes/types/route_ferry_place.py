"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryPlace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.position23
    import aws_sdk_geo_routes.types.sensitive_integer
    import aws_sdk_geo_routes.types.sensitive_string


class RouteFerryPlace(TypedDict, closed=True):
    name: NotRequired["aws_sdk_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The name of the place.</p>"""
    original_position: NotRequired["aws_sdk_geo_routes.types.position23.Position23"]
    """<p>Position provided in the request.</p>"""
    position: "aws_sdk_geo_routes.types.position23.Position23"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    waypoint_index: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Index of the waypoint in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryPlace) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "original_position" in value:
        import aws_sdk_geo_routes.types.position23

        out["OriginalPosition"] = aws_sdk_geo_routes.types.position23.serialize_json(
            value["original_position"]
        )
    import aws_sdk_geo_routes.types.position23

    out["Position"] = aws_sdk_geo_routes.types.position23.serialize_json(
        value["position"]
    )
    if "waypoint_index" in value:
        out["WaypointIndex"] = value["waypoint_index"]
    return out


def deserialize_json(data: dict) -> RouteFerryPlace:
    out: RouteFerryPlace = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "OriginalPosition" in data:
        import aws_sdk_geo_routes.types.position23

        out["original_position"] = aws_sdk_geo_routes.types.position23.deserialize_json(
            data["OriginalPosition"]
        )
    if "Position" in data:
        import aws_sdk_geo_routes.types.position23

        out["position"] = aws_sdk_geo_routes.types.position23.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RouteFerryPlace.position required")
    if "WaypointIndex" in data:
        out["waypoint_index"] = data["WaypointIndex"]
    return out
