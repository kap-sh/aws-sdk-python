"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLayerJoinDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_layer_color_field
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.unaggregated_field


class GeospatialLayerJoinDefinition(TypedDict):
    shape_key_field: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The name of the field or property in the geospatial data source.</p>"""
    dataset_key_field: NotRequired[
        "aws_sdk_quicksight.types.unaggregated_field.UnaggregatedField"
    ]
    color_field: NotRequired[
        "aws_sdk_quicksight.types.geospatial_layer_color_field.GeospatialLayerColorField"
    ]
    """<p>The geospatial color field for the join definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLayerJoinDefinition) -> dict:
    out: dict = {}
    if "shape_key_field" in value:
        out["ShapeKeyField"] = value["shape_key_field"]
    if "dataset_key_field" in value:
        import aws_sdk_quicksight.types.unaggregated_field

        out["DatasetKeyField"] = (
            aws_sdk_quicksight.types.unaggregated_field.serialize_json(
                value["dataset_key_field"]
            )
        )
    if "color_field" in value:
        import aws_sdk_quicksight.types.geospatial_layer_color_field

        out["ColorField"] = (
            aws_sdk_quicksight.types.geospatial_layer_color_field.serialize_json(
                value["color_field"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialLayerJoinDefinition:
    out: GeospatialLayerJoinDefinition = {}  # type: ignore[typeddict-item]
    if "ShapeKeyField" in data:
        out["shape_key_field"] = data["ShapeKeyField"]
    if "DatasetKeyField" in data:
        import aws_sdk_quicksight.types.unaggregated_field

        out["dataset_key_field"] = (
            aws_sdk_quicksight.types.unaggregated_field.deserialize_json(
                data["DatasetKeyField"]
            )
        )
    if "ColorField" in data:
        import aws_sdk_quicksight.types.geospatial_layer_color_field

        out["color_field"] = (
            aws_sdk_quicksight.types.geospatial_layer_color_field.deserialize_json(
                data["ColorField"]
            )
        )
    return out
