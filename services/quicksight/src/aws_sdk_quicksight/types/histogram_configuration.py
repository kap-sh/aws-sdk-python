"""Generated from Smithy shape ``com.amazonaws.quicksight#HistogramConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.axis_display_options
    import aws_sdk_quicksight.types.chart_axis_label_options
    import aws_sdk_quicksight.types.data_label_options
    import aws_sdk_quicksight.types.histogram_bin_options
    import aws_sdk_quicksight.types.histogram_field_wells
    import aws_sdk_quicksight.types.tooltip_options
    import aws_sdk_quicksight.types.visual_interaction_options
    import aws_sdk_quicksight.types.visual_palette


class HistogramConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.histogram_field_wells.HistogramFieldWells"
    ]
    """<p>The field well configuration of a histogram.</p>"""
    x_axis_display_options: NotRequired[
        "aws_sdk_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the x-axis.</p>"""
    x_axis_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The options that determine the presentation of the x-axis label.</p>"""
    y_axis_display_options: NotRequired[
        "aws_sdk_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the y-axis.</p>"""
    bin_options: NotRequired[
        "aws_sdk_quicksight.types.histogram_bin_options.HistogramBinOptions"
    ]
    """<p>The options that determine the presentation of histogram bins.</p>"""
    data_labels: NotRequired[
        "aws_sdk_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The data label configuration of a histogram.</p>"""
    tooltip: NotRequired["aws_sdk_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip configuration of a histogram.</p>"""
    visual_palette: NotRequired["aws_sdk_quicksight.types.visual_palette.VisualPalette"]
    """<p>The visual palette configuration of a histogram.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HistogramConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.histogram_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.histogram_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "x_axis_display_options" in value:
        import aws_sdk_quicksight.types.axis_display_options

        out["XAxisDisplayOptions"] = (
            aws_sdk_quicksight.types.axis_display_options.serialize_json(
                value["x_axis_display_options"]
            )
        )
    if "x_axis_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["XAxisLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["x_axis_label_options"]
            )
        )
    if "y_axis_display_options" in value:
        import aws_sdk_quicksight.types.axis_display_options

        out["YAxisDisplayOptions"] = (
            aws_sdk_quicksight.types.axis_display_options.serialize_json(
                value["y_axis_display_options"]
            )
        )
    if "bin_options" in value:
        import aws_sdk_quicksight.types.histogram_bin_options

        out["BinOptions"] = (
            aws_sdk_quicksight.types.histogram_bin_options.serialize_json(
                value["bin_options"]
            )
        )
    if "data_labels" in value:
        import aws_sdk_quicksight.types.data_label_options

        out["DataLabels"] = aws_sdk_quicksight.types.data_label_options.serialize_json(
            value["data_labels"]
        )
    if "tooltip" in value:
        import aws_sdk_quicksight.types.tooltip_options

        out["Tooltip"] = aws_sdk_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "visual_palette" in value:
        import aws_sdk_quicksight.types.visual_palette

        out["VisualPalette"] = aws_sdk_quicksight.types.visual_palette.serialize_json(
            value["visual_palette"]
        )
    if "interactions" in value:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> HistogramConfiguration:
    out: HistogramConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.histogram_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.histogram_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "XAxisDisplayOptions" in data:
        import aws_sdk_quicksight.types.axis_display_options

        out["x_axis_display_options"] = (
            aws_sdk_quicksight.types.axis_display_options.deserialize_json(
                data["XAxisDisplayOptions"]
            )
        )
    if "XAxisLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["x_axis_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["XAxisLabelOptions"]
            )
        )
    if "YAxisDisplayOptions" in data:
        import aws_sdk_quicksight.types.axis_display_options

        out["y_axis_display_options"] = (
            aws_sdk_quicksight.types.axis_display_options.deserialize_json(
                data["YAxisDisplayOptions"]
            )
        )
    if "BinOptions" in data:
        import aws_sdk_quicksight.types.histogram_bin_options

        out["bin_options"] = (
            aws_sdk_quicksight.types.histogram_bin_options.deserialize_json(
                data["BinOptions"]
            )
        )
    if "DataLabels" in data:
        import aws_sdk_quicksight.types.data_label_options

        out["data_labels"] = (
            aws_sdk_quicksight.types.data_label_options.deserialize_json(
                data["DataLabels"]
            )
        )
    if "Tooltip" in data:
        import aws_sdk_quicksight.types.tooltip_options

        out["tooltip"] = aws_sdk_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if "VisualPalette" in data:
        import aws_sdk_quicksight.types.visual_palette

        out["visual_palette"] = (
            aws_sdk_quicksight.types.visual_palette.deserialize_json(
                data["VisualPalette"]
            )
        )
    if "Interactions" in data:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.deserialize_json(
                data["Interactions"]
            )
        )
    return out
