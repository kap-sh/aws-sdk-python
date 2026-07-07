"""Generated from Smithy shape ``com.amazonaws.quicksight#BarChartConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.axis_display_options
    import aws_sdk_quicksight.types.bar_chart_default_series_settings
    import aws_sdk_quicksight.types.bar_chart_field_wells
    import aws_sdk_quicksight.types.bar_chart_orientation
    import aws_sdk_quicksight.types.bar_chart_sort_configuration
    import aws_sdk_quicksight.types.bar_series_item_list
    import aws_sdk_quicksight.types.bars_arrangement
    import aws_sdk_quicksight.types.chart_axis_label_options
    import aws_sdk_quicksight.types.contribution_analysis_default_list
    import aws_sdk_quicksight.types.data_label_options
    import aws_sdk_quicksight.types.legend_options
    import aws_sdk_quicksight.types.reference_line_list
    import aws_sdk_quicksight.types.small_multiples_options
    import aws_sdk_quicksight.types.tooltip_options
    import aws_sdk_quicksight.types.visual_interaction_options
    import aws_sdk_quicksight.types.visual_palette


class BarChartConfiguration(TypedDict, closed=True):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.bar_chart_field_wells.BarChartFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.bar_chart_sort_configuration.BarChartSortConfiguration"
    ]
    """<p>The sort configuration of a <code>BarChartVisual</code>.</p>"""
    orientation: NotRequired[
        "aws_sdk_quicksight.types.bar_chart_orientation.BarChartOrientation"
    ]
    """<p>The orientation of the bars in a bar chart visual. There are two valid values in this structure:</p> <ul> <li> <p> <code>HORIZONTAL</code>: Used for charts that have horizontal bars. Visuals that use this value are horizontal bar charts, horizontal stacked bar charts, and horizontal stacked 100% bar charts.</p> </li> <li> <p> <code>VERTICAL</code>: Used for charts that have vertical bars. Visuals that use this value are vertical bar charts, vertical stacked bar charts, and vertical stacked 100% bar charts.</p> </li> </ul>"""
    bars_arrangement: NotRequired[
        "aws_sdk_quicksight.types.bars_arrangement.BarsArrangement"
    ]
    """<p>Determines the arrangement of the bars. The orientation and arrangement of bars determine the type of bar that is used in the visual.</p>"""
    visual_palette: NotRequired["aws_sdk_quicksight.types.visual_palette.VisualPalette"]
    """<p>The palette (chart color) display setup of the visual.</p>"""
    small_multiples_options: NotRequired[
        "aws_sdk_quicksight.types.small_multiples_options.SmallMultiplesOptions"
    ]
    """<p>The small multiples setup for the visual.</p>"""
    category_axis: NotRequired[
        "aws_sdk_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, axis step) for bar chart category.</p>"""
    category_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility and sort icon visibility) for a bar chart.</p>"""
    value_axis: NotRequired[
        "aws_sdk_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The label display options (grid line, range, scale, axis step) for a bar chart value.</p>"""
    value_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility and sort icon visibility) for a bar chart value.</p>"""
    color_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options (label text, label visibility and sort icon visibility) for a color that is used in a bar chart.</p>"""
    default_series_settings: NotRequired[
        "aws_sdk_quicksight.types.bar_chart_default_series_settings.BarChartDefaultSeriesSettings"
    ]
    """<p>The options that determine the default presentation of all bar series in <code>BarChartVisual</code>.</p>"""
    series: NotRequired[
        "aws_sdk_quicksight.types.bar_series_item_list.BarSeriesItemList"
    ]
    """<p>The series item configuration of a <code>BarChartVisual</code>.</p>"""
    legend: NotRequired["aws_sdk_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    data_labels: NotRequired[
        "aws_sdk_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The options that determine if visual data labels are displayed.</p>"""
    tooltip: NotRequired["aws_sdk_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip display setup of the visual.</p>"""
    reference_lines: NotRequired[
        "aws_sdk_quicksight.types.reference_line_list.ReferenceLineList"
    ]
    """<p>The reference line setup of the visual.</p>"""
    contribution_analysis_defaults: NotRequired[
        "aws_sdk_quicksight.types.contribution_analysis_default_list.ContributionAnalysisDefaultList"
    ]
    """<p>The contribution analysis (anomaly configuration) setup of the visual.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BarChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.bar_chart_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.bar_chart_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.bar_chart_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.bar_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "orientation" in value:
        import aws_sdk_quicksight.types.bar_chart_orientation

        out["Orientation"] = (
            aws_sdk_quicksight.types.bar_chart_orientation.serialize_json(
                value["orientation"]
            )
        )
    if "bars_arrangement" in value:
        import aws_sdk_quicksight.types.bars_arrangement

        out["BarsArrangement"] = (
            aws_sdk_quicksight.types.bars_arrangement.serialize_json(
                value["bars_arrangement"]
            )
        )
    if "visual_palette" in value:
        import aws_sdk_quicksight.types.visual_palette

        out["VisualPalette"] = aws_sdk_quicksight.types.visual_palette.serialize_json(
            value["visual_palette"]
        )
    if "small_multiples_options" in value:
        import aws_sdk_quicksight.types.small_multiples_options

        out["SmallMultiplesOptions"] = (
            aws_sdk_quicksight.types.small_multiples_options.serialize_json(
                value["small_multiples_options"]
            )
        )
    if "category_axis" in value:
        import aws_sdk_quicksight.types.axis_display_options

        out["CategoryAxis"] = (
            aws_sdk_quicksight.types.axis_display_options.serialize_json(
                value["category_axis"]
            )
        )
    if "category_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["CategoryLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["category_label_options"]
            )
        )
    if "value_axis" in value:
        import aws_sdk_quicksight.types.axis_display_options

        out["ValueAxis"] = aws_sdk_quicksight.types.axis_display_options.serialize_json(
            value["value_axis"]
        )
    if "value_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["ValueLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["value_label_options"]
            )
        )
    if "color_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["ColorLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["color_label_options"]
            )
        )
    if "default_series_settings" in value:
        import aws_sdk_quicksight.types.bar_chart_default_series_settings

        out["DefaultSeriesSettings"] = (
            aws_sdk_quicksight.types.bar_chart_default_series_settings.serialize_json(
                value["default_series_settings"]
            )
        )
    if "series" in value:
        import aws_sdk_quicksight.types.bar_series_item_list

        out["Series"] = aws_sdk_quicksight.types.bar_series_item_list.serialize_json(
            value["series"]
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
    if "reference_lines" in value:
        import aws_sdk_quicksight.types.reference_line_list

        out["ReferenceLines"] = (
            aws_sdk_quicksight.types.reference_line_list.serialize_json(
                value["reference_lines"]
            )
        )
    if "contribution_analysis_defaults" in value:
        import aws_sdk_quicksight.types.contribution_analysis_default_list

        out["ContributionAnalysisDefaults"] = (
            aws_sdk_quicksight.types.contribution_analysis_default_list.serialize_json(
                value["contribution_analysis_defaults"]
            )
        )
    if "interactions" in value:
        import aws_sdk_quicksight.types.visual_interaction_options

        out["Interactions"] = (
            aws_sdk_quicksight.types.visual_interaction_options.serialize_json(
                value["interactions"]
            )
        )
    return out


def deserialize_json(data: dict) -> BarChartConfiguration:
    out: BarChartConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.bar_chart_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.bar_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.bar_chart_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.bar_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if "Orientation" in data:
        import aws_sdk_quicksight.types.bar_chart_orientation

        out["orientation"] = (
            aws_sdk_quicksight.types.bar_chart_orientation.deserialize_json(
                data["Orientation"]
            )
        )
    if "BarsArrangement" in data:
        import aws_sdk_quicksight.types.bars_arrangement

        out["bars_arrangement"] = (
            aws_sdk_quicksight.types.bars_arrangement.deserialize_json(
                data["BarsArrangement"]
            )
        )
    if "VisualPalette" in data:
        import aws_sdk_quicksight.types.visual_palette

        out["visual_palette"] = (
            aws_sdk_quicksight.types.visual_palette.deserialize_json(
                data["VisualPalette"]
            )
        )
    if "SmallMultiplesOptions" in data:
        import aws_sdk_quicksight.types.small_multiples_options

        out["small_multiples_options"] = (
            aws_sdk_quicksight.types.small_multiples_options.deserialize_json(
                data["SmallMultiplesOptions"]
            )
        )
    if "CategoryAxis" in data:
        import aws_sdk_quicksight.types.axis_display_options

        out["category_axis"] = (
            aws_sdk_quicksight.types.axis_display_options.deserialize_json(
                data["CategoryAxis"]
            )
        )
    if "CategoryLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["category_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["CategoryLabelOptions"]
            )
        )
    if "ValueAxis" in data:
        import aws_sdk_quicksight.types.axis_display_options

        out["value_axis"] = (
            aws_sdk_quicksight.types.axis_display_options.deserialize_json(
                data["ValueAxis"]
            )
        )
    if "ValueLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["value_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["ValueLabelOptions"]
            )
        )
    if "ColorLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["color_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["ColorLabelOptions"]
            )
        )
    if "DefaultSeriesSettings" in data:
        import aws_sdk_quicksight.types.bar_chart_default_series_settings

        out["default_series_settings"] = (
            aws_sdk_quicksight.types.bar_chart_default_series_settings.deserialize_json(
                data["DefaultSeriesSettings"]
            )
        )
    if "Series" in data:
        import aws_sdk_quicksight.types.bar_series_item_list

        out["series"] = aws_sdk_quicksight.types.bar_series_item_list.deserialize_json(
            data["Series"]
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
    if "ReferenceLines" in data:
        import aws_sdk_quicksight.types.reference_line_list

        out["reference_lines"] = (
            aws_sdk_quicksight.types.reference_line_list.deserialize_json(
                data["ReferenceLines"]
            )
        )
    if "ContributionAnalysisDefaults" in data:
        import aws_sdk_quicksight.types.contribution_analysis_default_list

        out["contribution_analysis_defaults"] = (
            aws_sdk_quicksight.types.contribution_analysis_default_list.deserialize_json(
                data["ContributionAnalysisDefaults"]
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
