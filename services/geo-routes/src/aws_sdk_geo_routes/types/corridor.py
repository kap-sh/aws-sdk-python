"""Generated from Smithy shape ``com.amazonaws.georoutes#Corridor``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.line_string


class Corridor(TypedDict):
    line_string: "aws_sdk_geo_routes.types.line_string.LineString"
    """<p>An ordered list of positions used to plot a route on a map.</p> <note> <p>LineString and Polyline are mutually exclusive properties.</p> </note>"""
    radius: "int"
    """<p>Radius that defines the width of the corridor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Corridor) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.line_string

    out["LineString"] = aws_sdk_geo_routes.types.line_string.serialize_json(
        value["line_string"]
    )
    out["Radius"] = value["radius"]
    return out


def deserialize_json(data: dict) -> Corridor:
    out: Corridor = {}  # type: ignore[typeddict-item]
    if "LineString" in data:
        import aws_sdk_geo_routes.types.line_string

        out["line_string"] = aws_sdk_geo_routes.types.line_string.deserialize_json(
            data["LineString"]
        )
    else:
        raise DeserializationError("Corridor.line_string required")
    if "Radius" in data:
        out["radius"] = data["Radius"]
    else:
        raise DeserializationError("Corridor.radius required")
    return out
