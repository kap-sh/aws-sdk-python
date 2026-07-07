"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arc_axis_configuration
    import aws_sdk_quicksight.types.arc_configuration
    import aws_sdk_quicksight.types.comparison_configuration
    import aws_sdk_quicksight.types.font_configuration
    import aws_sdk_quicksight.types.primary_value_display_type


class GaugeChartOptions(TypedDict, closed=True):
    primary_value_display_type: NotRequired[
        "aws_sdk_quicksight.types.primary_value_display_type.PrimaryValueDisplayType"
    ]
    """<p>The options that determine the primary value display type.</p>"""
    comparison: NotRequired[
        "aws_sdk_quicksight.types.comparison_configuration.ComparisonConfiguration"
    ]
    """<p>The comparison configuration of a <code>GaugeChartVisual</code>.</p>"""
    arc_axis: NotRequired[
        "aws_sdk_quicksight.types.arc_axis_configuration.ArcAxisConfiguration"
    ]
    """<p>The arc axis configuration of a <code>GaugeChartVisual</code>.</p>"""
    arc: NotRequired["aws_sdk_quicksight.types.arc_configuration.ArcConfiguration"]
    """<p>The arc configuration of a <code>GaugeChartVisual</code>.</p>"""
    primary_value_font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>The options that determine the primary value font configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartOptions) -> dict:
    out: dict = {}
    if "primary_value_display_type" in value:
        import aws_sdk_quicksight.types.primary_value_display_type

        out["PrimaryValueDisplayType"] = (
            aws_sdk_quicksight.types.primary_value_display_type.serialize_json(
                value["primary_value_display_type"]
            )
        )
    if "comparison" in value:
        import aws_sdk_quicksight.types.comparison_configuration

        out["Comparison"] = (
            aws_sdk_quicksight.types.comparison_configuration.serialize_json(
                value["comparison"]
            )
        )
    if "arc_axis" in value:
        import aws_sdk_quicksight.types.arc_axis_configuration

        out["ArcAxis"] = aws_sdk_quicksight.types.arc_axis_configuration.serialize_json(
            value["arc_axis"]
        )
    if "arc" in value:
        import aws_sdk_quicksight.types.arc_configuration

        out["Arc"] = aws_sdk_quicksight.types.arc_configuration.serialize_json(
            value["arc"]
        )
    if "primary_value_font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["PrimaryValueFontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["primary_value_font_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GaugeChartOptions:
    out: GaugeChartOptions = {}  # type: ignore[typeddict-item]
    if "PrimaryValueDisplayType" in data:
        import aws_sdk_quicksight.types.primary_value_display_type

        out["primary_value_display_type"] = (
            aws_sdk_quicksight.types.primary_value_display_type.deserialize_json(
                data["PrimaryValueDisplayType"]
            )
        )
    if "Comparison" in data:
        import aws_sdk_quicksight.types.comparison_configuration

        out["comparison"] = (
            aws_sdk_quicksight.types.comparison_configuration.deserialize_json(
                data["Comparison"]
            )
        )
    if "ArcAxis" in data:
        import aws_sdk_quicksight.types.arc_axis_configuration

        out["arc_axis"] = (
            aws_sdk_quicksight.types.arc_axis_configuration.deserialize_json(
                data["ArcAxis"]
            )
        )
    if "Arc" in data:
        import aws_sdk_quicksight.types.arc_configuration

        out["arc"] = aws_sdk_quicksight.types.arc_configuration.deserialize_json(
            data["Arc"]
        )
    if "PrimaryValueFontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["primary_value_font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["PrimaryValueFontConfiguration"]
            )
        )
    return out
