"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineShapeGeometry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.linear_rings
    import aws_sdk_geo_routes.types.polyline_ring_list


class IsolineShapeGeometry(TypedDict):
    polygon: NotRequired["aws_sdk_geo_routes.types.linear_rings.LinearRings"]
    """<p>A series of coordinate rings defining the reachable area when Simple geometry format is requested. Each ring is a list of <code>[longitude, latitude]</code> coordinate pairs. The first ring defines the outer boundary; subsequent rings define holes representing unreachable areas.</p> <note> <p>Polygon and PolylinePolygon are mutually exclusive properties.</p> </note>"""
    polyline_polygon: NotRequired[
        "aws_sdk_geo_routes.types.polyline_ring_list.PolylineRingList"
    ]
    r"""<p>An encoded representation of the reachable area when FlexiblePolyline geometry format is requested. Provides a compact representation suitable for transmission and storage. The first string defines the outer boundary; subsequent strings define holes representing unreachable areas. For more information on polyline encoding, see <a href=\"https://github.com/aws-geospatial/polyline\">https://github.com/aws-geospatial/polyline</a>.</p> <note> <p>Polygon and PolylinePolygon are mutually exclusive properties.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineShapeGeometry) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> IsolineShapeGeometry:
    out: IsolineShapeGeometry = {}  # type: ignore[typeddict-item]
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
