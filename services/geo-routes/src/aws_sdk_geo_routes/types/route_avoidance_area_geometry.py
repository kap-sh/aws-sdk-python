"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAvoidanceAreaGeometry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.bounding_box
    import aws_sdk_geo_routes.types.corridor
    import aws_sdk_geo_routes.types.linear_rings
    import aws_sdk_geo_routes.types.polyline_corridor
    import aws_sdk_geo_routes.types.polyline_ring_list


class RouteAvoidanceAreaGeometry(TypedDict):
    corridor: NotRequired["aws_sdk_geo_routes.types.corridor.Corridor"]
    """<p>Geometry defined as a corridor - a LineString with a radius that defines the width of the corridor.</p>"""
    bounding_box: NotRequired["aws_sdk_geo_routes.types.bounding_box.BoundingBox"]
    """<p>Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.</p>"""
    polygon: NotRequired["aws_sdk_geo_routes.types.linear_rings.LinearRings"]
    """<p>Geometry defined as a polygon with only one linear ring.</p>"""
    polyline_corridor: NotRequired[
        "aws_sdk_geo_routes.types.polyline_corridor.PolylineCorridor"
    ]
    """<p>Geometry defined as an encoded corridor - an encoded polyline with a radius that defines the width of the corridor.</p>"""
    polyline_polygon: NotRequired[
        "aws_sdk_geo_routes.types.polyline_ring_list.PolylineRingList"
    ]
    """<p>A list of Isoline PolylinePolygon, for each isoline PolylinePolygon, it contains PolylinePolygon of the first linear ring (the outer ring) and from 2nd item to the last item (the inner rings). For more information on polyline encoding, see <a href=\"https://github.com/aws-geospatial/polyline\">https://github.com/aws-geospatial/polyline</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAvoidanceAreaGeometry) -> dict:
    out: dict = {}
    if "corridor" in value:
        import aws_sdk_geo_routes.types.corridor

        out["Corridor"] = aws_sdk_geo_routes.types.corridor.serialize_json(
            value["corridor"]
        )
    if "bounding_box" in value:
        import aws_sdk_geo_routes.types.bounding_box

        out["BoundingBox"] = aws_sdk_geo_routes.types.bounding_box.serialize_json(
            value["bounding_box"]
        )
    if "polygon" in value:
        import aws_sdk_geo_routes.types.linear_rings

        out["Polygon"] = aws_sdk_geo_routes.types.linear_rings.serialize_json(
            value["polygon"]
        )
    if "polyline_corridor" in value:
        import aws_sdk_geo_routes.types.polyline_corridor

        out["PolylineCorridor"] = (
            aws_sdk_geo_routes.types.polyline_corridor.serialize_json(
                value["polyline_corridor"]
            )
        )
    if "polyline_polygon" in value:
        import aws_sdk_geo_routes.types.polyline_ring_list

        out["PolylinePolygon"] = (
            aws_sdk_geo_routes.types.polyline_ring_list.serialize_json(
                value["polyline_polygon"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteAvoidanceAreaGeometry:
    out: RouteAvoidanceAreaGeometry = {}  # type: ignore[typeddict-item]
    if "Corridor" in data:
        import aws_sdk_geo_routes.types.corridor

        out["corridor"] = aws_sdk_geo_routes.types.corridor.deserialize_json(
            data["Corridor"]
        )
    if "BoundingBox" in data:
        import aws_sdk_geo_routes.types.bounding_box

        out["bounding_box"] = aws_sdk_geo_routes.types.bounding_box.deserialize_json(
            data["BoundingBox"]
        )
    if "Polygon" in data:
        import aws_sdk_geo_routes.types.linear_rings

        out["polygon"] = aws_sdk_geo_routes.types.linear_rings.deserialize_json(
            data["Polygon"]
        )
    if "PolylineCorridor" in data:
        import aws_sdk_geo_routes.types.polyline_corridor

        out["polyline_corridor"] = (
            aws_sdk_geo_routes.types.polyline_corridor.deserialize_json(
                data["PolylineCorridor"]
            )
        )
    if "PolylinePolygon" in data:
        import aws_sdk_geo_routes.types.polyline_ring_list

        out["polyline_polygon"] = (
            aws_sdk_geo_routes.types.polyline_ring_list.deserialize_json(
                data["PolylinePolygon"]
            )
        )
    return out
