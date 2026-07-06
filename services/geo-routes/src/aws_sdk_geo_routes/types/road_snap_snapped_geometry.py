"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapSnappedGeometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.line_string
    import aws_sdk_geo_routes.types.polyline


class RoadSnapSnappedGeometry(TypedDict, closed=True):
    line_string: NotRequired["aws_sdk_geo_routes.types.line_string.LineString"]
    """<p>An ordered list of positions used to plot a route on a map.</p> <note> <p>LineString and Polyline are mutually exclusive properties.</p> </note>"""
    polyline: NotRequired["aws_sdk_geo_routes.types.polyline.Polyline"]
    """<p>An ordered list of positions used to plot a route on a map in a lossy compression format.</p> <note> <p>LineString and Polyline are mutually exclusive properties.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapSnappedGeometry) -> dict:
    out: dict = {}
    if "line_string" in value:
        import aws_sdk_geo_routes.types.line_string

        out["LineString"] = aws_sdk_geo_routes.types.line_string.serialize_json(
            value["line_string"]
        )
    if "polyline" in value:
        out["Polyline"] = value["polyline"]
    return out


def deserialize_json(data: dict) -> RoadSnapSnappedGeometry:
    out: RoadSnapSnappedGeometry = {}  # type: ignore[typeddict-item]
    if "LineString" in data:
        import aws_sdk_geo_routes.types.line_string

        out["line_string"] = aws_sdk_geo_routes.types.line_string.deserialize_json(
            data["LineString"]
        )
    if "Polyline" in data:
        out["polyline"] = data["Polyline"]
    return out
