"""Generated from Smithy shape ``com.amazonaws.quicksight#ScatterPlotConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.axis_display_options
    import aws_sdk_quicksight.types.chart_axis_label_options
    import aws_sdk_quicksight.types.data_label_options
    import aws_sdk_quicksight.types.legend_options
    import aws_sdk_quicksight.types.scatter_plot_field_wells
    import aws_sdk_quicksight.types.scatter_plot_sort_configuration
    import aws_sdk_quicksight.types.tooltip_options
    import aws_sdk_quicksight.types.visual_interaction_options
    import aws_sdk_quicksight.types.visual_palette


class ScatterPlotConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.scatter_plot_field_wells.ScatterPlotFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.scatter_plot_sort_configuration.ScatterPlotSortConfiguration"
    ]
    """<p>The sort configuration of a scatter plot.</p>"""
    x_axis_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility, and sort icon visibility) of the scatter plot's x-axis.</p>"""
    x_axis_display_options: NotRequired[
        "aws_sdk_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, and axis step) of the scatter plot's x-axis.</p>"""
    y_axis_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility, and sort icon visibility) of the scatter plot's y-axis.</p>"""
    y_axis_display_options: NotRequired[
        "aws_sdk_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, and axis step) of the scatter plot's y-axis.</p>"""
    legend: NotRequired["aws_sdk_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    data_labels: NotRequired[
        "aws_sdk_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The options that determine if visual data labels are displayed.</p>"""
    tooltip: NotRequired["aws_sdk_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The legend display setup of the visual.</p>"""
    visual_palette: NotRequired["aws_sdk_quicksight.types.visual_palette.VisualPalette"]
    """<p>The palette (chart color) display setup of the visual.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScatterPlotConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.scatter_plot_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.scatter_plot_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.scatter_plot_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.scatter_plot_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "x_axis_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["XAxisLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["x_axis_label_options"]
            )
        )
    if "x_axis_display_options" in value:
        import aws_sdk_quicksight.types.axis_display_options

        out["XAxisDisplayOptions"] = (
            aws_sdk_quicksight.types.axis_display_options.serialize_json(
                value["x_axis_display_options"]
            )
        )
    if "y_axis_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["YAxisLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["y_axis_label_options"]
            )
        )
    if "y_axis_display_options" in value:
        import aws_sdk_quicksight.types.axis_display_options

        out["YAxisDisplayOptions"] = (
            aws_sdk_quicksight.types.axis_display_options.serialize_json(
                value["y_axis_display_options"]
            )
        )
    if "legend" in value:
        import aws_sdk_quicksight.types.legend_options

        out["Legend"] = aws_sdk_quicksight.types.legend_options.serialize_json(
            value["legend"]
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


def deserialize_json(data: dict) -> ScatterPlotConfiguration:
    out: ScatterPlotConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.scatter_plot_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.scatter_plot_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.scatter_plot_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.scatter_plot_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if "XAxisLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["x_axis_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["XAxisLabelOptions"]
            )
        )
    if "XAxisDisplayOptions" in data:
        import aws_sdk_quicksight.types.axis_display_options

        out["x_axis_display_options"] = (
            aws_sdk_quicksight.types.axis_display_options.deserialize_json(
                data["XAxisDisplayOptions"]
            )
        )
    if "YAxisLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["y_axis_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["YAxisLabelOptions"]
            )
        )
    if "YAxisDisplayOptions" in data:
        import aws_sdk_quicksight.types.axis_display_options

        out["y_axis_display_options"] = (
            aws_sdk_quicksight.types.axis_display_options.deserialize_json(
                data["YAxisDisplayOptions"]
            )
        )
    if "Legend" in data:
        import aws_sdk_quicksight.types.legend_options

        out["legend"] = aws_sdk_quicksight.types.legend_options.deserialize_json(
            data["Legend"]
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
