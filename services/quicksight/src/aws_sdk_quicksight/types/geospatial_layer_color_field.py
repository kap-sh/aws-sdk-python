"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLayerColorField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_layer_dimension_field_list
    import aws_sdk_quicksight.types.geospatial_layer_measure_field_list


class GeospatialLayerColorField(TypedDict, closed=True):
    color_dimensions_fields: NotRequired[
        "aws_sdk_quicksight.types.geospatial_layer_dimension_field_list.GeospatialLayerDimensionFieldList"
    ]
    """<p>A list of color dimension fields.</p>"""
    color_values_fields: NotRequired[
        "aws_sdk_quicksight.types.geospatial_layer_measure_field_list.GeospatialLayerMeasureFieldList"
    ]
    """<p>A list of color measure fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLayerColorField) -> dict:
    out: dict = {}
    if "color_dimensions_fields" in value:
        import aws_sdk_quicksight.types.geospatial_layer_dimension_field_list

        out["ColorDimensionsFields"] = (
            aws_sdk_quicksight.types.geospatial_layer_dimension_field_list.serialize_json(
                value["color_dimensions_fields"]
            )
        )
    if "color_values_fields" in value:
        import aws_sdk_quicksight.types.geospatial_layer_measure_field_list

        out["ColorValuesFields"] = (
            aws_sdk_quicksight.types.geospatial_layer_measure_field_list.serialize_json(
                value["color_values_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialLayerColorField:
    out: GeospatialLayerColorField = {}  # type: ignore[typeddict-item]
    if "ColorDimensionsFields" in data:
        import aws_sdk_quicksight.types.geospatial_layer_dimension_field_list

        out["color_dimensions_fields"] = (
            aws_sdk_quicksight.types.geospatial_layer_dimension_field_list.deserialize_json(
                data["ColorDimensionsFields"]
            )
        )
    if "ColorValuesFields" in data:
        import aws_sdk_quicksight.types.geospatial_layer_measure_field_list

        out["color_values_fields"] = (
            aws_sdk_quicksight.types.geospatial_layer_measure_field_list.deserialize_json(
                data["ColorValuesFields"]
            )
        )
    return out
