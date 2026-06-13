"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLayerDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_line_layer
    import aws_sdk_quicksight.types.geospatial_point_layer
    import aws_sdk_quicksight.types.geospatial_polygon_layer


class GeospatialLayerDefinition(TypedDict):
    point_layer: NotRequired[
        "aws_sdk_quicksight.types.geospatial_point_layer.GeospatialPointLayer"
    ]
    """<p>The definition for a point layer.</p>"""
    line_layer: NotRequired[
        "aws_sdk_quicksight.types.geospatial_line_layer.GeospatialLineLayer"
    ]
    """<p>The definition for a line layer.</p>"""
    polygon_layer: NotRequired[
        "aws_sdk_quicksight.types.geospatial_polygon_layer.GeospatialPolygonLayer"
    ]
    """<p>The definition for a polygon layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLayerDefinition) -> dict:
    out: dict = {}
    if "point_layer" in value:
        import aws_sdk_quicksight.types.geospatial_point_layer

        out["PointLayer"] = (
            aws_sdk_quicksight.types.geospatial_point_layer.serialize_json(
                value["point_layer"]
            )
        )
    if "line_layer" in value:
        import aws_sdk_quicksight.types.geospatial_line_layer

        out["LineLayer"] = (
            aws_sdk_quicksight.types.geospatial_line_layer.serialize_json(
                value["line_layer"]
            )
        )
    if "polygon_layer" in value:
        import aws_sdk_quicksight.types.geospatial_polygon_layer

        out["PolygonLayer"] = (
            aws_sdk_quicksight.types.geospatial_polygon_layer.serialize_json(
                value["polygon_layer"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialLayerDefinition:
    out: GeospatialLayerDefinition = {}  # type: ignore[typeddict-item]
    if "PointLayer" in data:
        import aws_sdk_quicksight.types.geospatial_point_layer

        out["point_layer"] = (
            aws_sdk_quicksight.types.geospatial_point_layer.deserialize_json(
                data["PointLayer"]
            )
        )
    if "LineLayer" in data:
        import aws_sdk_quicksight.types.geospatial_line_layer

        out["line_layer"] = (
            aws_sdk_quicksight.types.geospatial_line_layer.deserialize_json(
                data["LineLayer"]
            )
        )
    if "PolygonLayer" in data:
        import aws_sdk_quicksight.types.geospatial_polygon_layer

        out["polygon_layer"] = (
            aws_sdk_quicksight.types.geospatial_polygon_layer.deserialize_json(
                data["PolygonLayer"]
            )
        )
    return out
