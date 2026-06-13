"""Generated from Smithy shape ``com.amazonaws.quicksight#PluginVisualFieldWell``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field_list
    import aws_sdk_quicksight.types.measure_field_list
    import aws_sdk_quicksight.types.plugin_visual_axis_name
    import aws_sdk_quicksight.types.unaggregated_field_list


class PluginVisualFieldWell(TypedDict):
    axis_name: NotRequired[
        "aws_sdk_quicksight.types.plugin_visual_axis_name.PluginVisualAxisName"
    ]
    """<p>The semantic axis name for the field well.</p>"""
    dimensions: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>A list of dimensions for the field well.</p>"""
    measures: NotRequired[
        "aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"
    ]
    """<p>A list of measures that exist in the field well.</p>"""
    unaggregated: NotRequired[
        "aws_sdk_quicksight.types.unaggregated_field_list.UnaggregatedFieldList"
    ]
    """<p>A list of unaggregated fields that exist in the field well.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PluginVisualFieldWell) -> dict:
    out: dict = {}
    if "axis_name" in value:
        import aws_sdk_quicksight.types.plugin_visual_axis_name

        out["AxisName"] = (
            aws_sdk_quicksight.types.plugin_visual_axis_name.serialize_json(
                value["axis_name"]
            )
        )
    if "dimensions" in value:
        import aws_sdk_quicksight.types.dimension_field_list

        out["Dimensions"] = (
            aws_sdk_quicksight.types.dimension_field_list.serialize_json(
                value["dimensions"]
            )
        )
    if "measures" in value:
        import aws_sdk_quicksight.types.measure_field_list

        out["Measures"] = aws_sdk_quicksight.types.measure_field_list.serialize_json(
            value["measures"]
        )
    if "unaggregated" in value:
        import aws_sdk_quicksight.types.unaggregated_field_list

        out["Unaggregated"] = (
            aws_sdk_quicksight.types.unaggregated_field_list.serialize_json(
                value["unaggregated"]
            )
        )
    return out


def deserialize_json(data: dict) -> PluginVisualFieldWell:
    out: PluginVisualFieldWell = {}  # type: ignore[typeddict-item]
    if "AxisName" in data:
        import aws_sdk_quicksight.types.plugin_visual_axis_name

        out["axis_name"] = (
            aws_sdk_quicksight.types.plugin_visual_axis_name.deserialize_json(
                data["AxisName"]
            )
        )
    if "Dimensions" in data:
        import aws_sdk_quicksight.types.dimension_field_list

        out["dimensions"] = (
            aws_sdk_quicksight.types.dimension_field_list.deserialize_json(
                data["Dimensions"]
            )
        )
    if "Measures" in data:
        import aws_sdk_quicksight.types.measure_field_list

        out["measures"] = aws_sdk_quicksight.types.measure_field_list.deserialize_json(
            data["Measures"]
        )
    if "Unaggregated" in data:
        import aws_sdk_quicksight.types.unaggregated_field_list

        out["unaggregated"] = (
            aws_sdk_quicksight.types.unaggregated_field_list.deserialize_json(
                data["Unaggregated"]
            )
        )
    return out
