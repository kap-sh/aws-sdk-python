"""Generated from Smithy shape ``com.amazonaws.quicksight#SparklinesOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.hex_color
    import aws_sdk_quicksight.types.line_chart_marker_style_settings
    import aws_sdk_quicksight.types.line_interpolation
    import aws_sdk_quicksight.types.sparkline_axis_behavior
    import aws_sdk_quicksight.types.sparkline_visual_type


class SparklinesOptions(TypedDict):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The field ID of the value column that the sparkline is applied to.</p>"""
    x_axis_field: "aws_sdk_quicksight.types.dimension_field.DimensionField"
    y_axis_behavior: NotRequired[
        "aws_sdk_quicksight.types.sparkline_axis_behavior.SparklineAxisBehavior"
    ]
    """<p>Determines whether the Y axis is shared across all sparklines or independent for each sparkline.</p>"""
    visual_type: NotRequired[
        "aws_sdk_quicksight.types.sparkline_visual_type.SparklineVisualType"
    ]
    """<p>The type of the sparkline. Valid values are <code>LINE</code> and <code>AREA_LINE</code>.</p>"""
    line_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The color of the sparkline line.</p>"""
    line_interpolation: NotRequired[
        "aws_sdk_quicksight.types.line_interpolation.LineInterpolation"
    ]
    """<p>The interpolation style for the sparkline line.</p>"""
    all_points_marker: NotRequired[
        "aws_sdk_quicksight.types.line_chart_marker_style_settings.LineChartMarkerStyleSettings"
    ]
    max_value_marker: NotRequired[
        "aws_sdk_quicksight.types.line_chart_marker_style_settings.LineChartMarkerStyleSettings"
    ]
    min_value_marker: NotRequired[
        "aws_sdk_quicksight.types.line_chart_marker_style_settings.LineChartMarkerStyleSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SparklinesOptions) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import aws_sdk_quicksight.types.dimension_field

    out["XAxisField"] = aws_sdk_quicksight.types.dimension_field.serialize_json(
        value["x_axis_field"]
    )
    if "y_axis_behavior" in value:
        import aws_sdk_quicksight.types.sparkline_axis_behavior

        out["YAxisBehavior"] = (
            aws_sdk_quicksight.types.sparkline_axis_behavior.serialize_json(
                value["y_axis_behavior"]
            )
        )
    if "visual_type" in value:
        import aws_sdk_quicksight.types.sparkline_visual_type

        out["VisualType"] = (
            aws_sdk_quicksight.types.sparkline_visual_type.serialize_json(
                value["visual_type"]
            )
        )
    if "line_color" in value:
        out["LineColor"] = value["line_color"]
    if "line_interpolation" in value:
        import aws_sdk_quicksight.types.line_interpolation

        out["LineInterpolation"] = (
            aws_sdk_quicksight.types.line_interpolation.serialize_json(
                value["line_interpolation"]
            )
        )
    if "all_points_marker" in value:
        import aws_sdk_quicksight.types.line_chart_marker_style_settings

        out["AllPointsMarker"] = (
            aws_sdk_quicksight.types.line_chart_marker_style_settings.serialize_json(
                value["all_points_marker"]
            )
        )
    if "max_value_marker" in value:
        import aws_sdk_quicksight.types.line_chart_marker_style_settings

        out["MaxValueMarker"] = (
            aws_sdk_quicksight.types.line_chart_marker_style_settings.serialize_json(
                value["max_value_marker"]
            )
        )
    if "min_value_marker" in value:
        import aws_sdk_quicksight.types.line_chart_marker_style_settings

        out["MinValueMarker"] = (
            aws_sdk_quicksight.types.line_chart_marker_style_settings.serialize_json(
                value["min_value_marker"]
            )
        )
    return out


def deserialize_json(data: dict) -> SparklinesOptions:
    out: SparklinesOptions = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("SparklinesOptions.field_id required")
    if "XAxisField" in data:
        import aws_sdk_quicksight.types.dimension_field

        out["x_axis_field"] = aws_sdk_quicksight.types.dimension_field.deserialize_json(
            data["XAxisField"]
        )
    else:
        raise DeserializationError("SparklinesOptions.x_axis_field required")
    if "YAxisBehavior" in data:
        import aws_sdk_quicksight.types.sparkline_axis_behavior

        out["y_axis_behavior"] = (
            aws_sdk_quicksight.types.sparkline_axis_behavior.deserialize_json(
                data["YAxisBehavior"]
            )
        )
    if "VisualType" in data:
        import aws_sdk_quicksight.types.sparkline_visual_type

        out["visual_type"] = (
            aws_sdk_quicksight.types.sparkline_visual_type.deserialize_json(
                data["VisualType"]
            )
        )
    if "LineColor" in data:
        out["line_color"] = data["LineColor"]
    if "LineInterpolation" in data:
        import aws_sdk_quicksight.types.line_interpolation

        out["line_interpolation"] = (
            aws_sdk_quicksight.types.line_interpolation.deserialize_json(
                data["LineInterpolation"]
            )
        )
    if "AllPointsMarker" in data:
        import aws_sdk_quicksight.types.line_chart_marker_style_settings

        out["all_points_marker"] = (
            aws_sdk_quicksight.types.line_chart_marker_style_settings.deserialize_json(
                data["AllPointsMarker"]
            )
        )
    if "MaxValueMarker" in data:
        import aws_sdk_quicksight.types.line_chart_marker_style_settings

        out["max_value_marker"] = (
            aws_sdk_quicksight.types.line_chart_marker_style_settings.deserialize_json(
                data["MaxValueMarker"]
            )
        )
    if "MinValueMarker" in data:
        import aws_sdk_quicksight.types.line_chart_marker_style_settings

        out["min_value_marker"] = (
            aws_sdk_quicksight.types.line_chart_marker_style_settings.deserialize_json(
                data["MinValueMarker"]
            )
        )
    return out
