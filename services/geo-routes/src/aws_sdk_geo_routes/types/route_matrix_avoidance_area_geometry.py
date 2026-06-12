"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAvoidanceAreaGeometry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.bounding_box
    import aws_sdk_geo_routes.types.linear_rings
    import aws_sdk_geo_routes.types.polyline_ring_list


class RouteMatrixAvoidanceAreaGeometry(TypedDict):
    bounding_box: NotRequired["aws_sdk_geo_routes.types.bounding_box.BoundingBox"]
    """<p>Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.</p>"""
    polygon: NotRequired["aws_sdk_geo_routes.types.linear_rings.LinearRings"]
    """<p>Geometry defined as a polygon with only one linear ring.</p>"""
    polyline_polygon: NotRequired[
        "aws_sdk_geo_routes.types.polyline_ring_list.PolylineRingList"
    ]
    """<p>A list of Isoline PolylinePolygon, for each isoline PolylinePolygon, it contains PolylinePolygon of the first linear ring (the outer ring) and from second item to the last item (the inner rings). For more information on polyline encoding, see <a href=\"https://github.com/aws-geospatial/polyline\">https://github.com/aws-geospatial/polyline</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAvoidanceAreaGeometry) -> dict:
    out: dict = {}
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
    if "polyline_polygon" in value:
        import aws_sdk_geo_routes.types.polyline_ring_list

        out["PolylinePolygon"] = (
            aws_sdk_geo_routes.types.polyline_ring_list.serialize_json(
                value["polyline_polygon"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixAvoidanceAreaGeometry:
    out: RouteMatrixAvoidanceAreaGeometry = {}  # type: ignore[typeddict-item]
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
    if "PolylinePolygon" in data:
        import aws_sdk_geo_routes.types.polyline_ring_list

        out["polyline_polygon"] = (
            aws_sdk_geo_routes.types.polyline_ring_list.deserialize_json(
                data["PolylinePolygon"]
            )
        )
    return out
