"""Generated from Smithy shape ``com.amazonaws.quicksight#PieChartConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.chart_axis_label_options
    import aws_sdk_quicksight.types.contribution_analysis_default_list
    import aws_sdk_quicksight.types.data_label_options
    import aws_sdk_quicksight.types.donut_options
    import aws_sdk_quicksight.types.legend_options
    import aws_sdk_quicksight.types.pie_chart_field_wells
    import aws_sdk_quicksight.types.pie_chart_sort_configuration
    import aws_sdk_quicksight.types.small_multiples_options
    import aws_sdk_quicksight.types.tooltip_options
    import aws_sdk_quicksight.types.visual_interaction_options
    import aws_sdk_quicksight.types.visual_palette


class PieChartConfiguration(TypedDict):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.pie_chart_field_wells.PieChartFieldWells"
    ]
    """<p>The field wells of the visual.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.pie_chart_sort_configuration.PieChartSortConfiguration"
    ]
    """<p>The sort configuration of a pie chart.</p>"""
    donut_options: NotRequired["aws_sdk_quicksight.types.donut_options.DonutOptions"]
    """<p>The options that determine the shape of the chart. This option determines whether the chart is a pie chart or a donut chart.</p>"""
    small_multiples_options: NotRequired[
        "aws_sdk_quicksight.types.small_multiples_options.SmallMultiplesOptions"
    ]
    """<p>The small multiples setup for the visual.</p>"""
    category_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options of the group/color that is displayed in a pie chart.</p>"""
    value_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options for the value that is displayed in a pie chart.</p>"""
    legend: NotRequired["aws_sdk_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    data_labels: NotRequired[
        "aws_sdk_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The options that determine if visual data labels are displayed.</p>"""
    tooltip: NotRequired["aws_sdk_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip display setup of the visual.</p>"""
    visual_palette: NotRequired["aws_sdk_quicksight.types.visual_palette.VisualPalette"]
    """<p>The palette (chart color) display setup of the visual.</p>"""
    contribution_analysis_defaults: NotRequired[
        "aws_sdk_quicksight.types.contribution_analysis_default_list.ContributionAnalysisDefaultList"
    ]
    """<p>The contribution analysis (anomaly configuration) setup of the visual.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PieChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.pie_chart_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.pie_chart_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.pie_chart_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.pie_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "donut_options" in value:
        import aws_sdk_quicksight.types.donut_options

        out["DonutOptions"] = aws_sdk_quicksight.types.donut_options.serialize_json(
            value["donut_options"]
        )
    if "small_multiples_options" in value:
        import aws_sdk_quicksight.types.small_multiples_options

        out["SmallMultiplesOptions"] = (
            aws_sdk_quicksight.types.small_multiples_options.serialize_json(
                value["small_multiples_options"]
            )
        )
    if "category_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["CategoryLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["category_label_options"]
            )
        )
    if "value_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["ValueLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["value_label_options"]
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


def deserialize_json(data: dict) -> PieChartConfiguration:
    out: PieChartConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.pie_chart_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.pie_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.pie_chart_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.pie_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if "DonutOptions" in data:
        import aws_sdk_quicksight.types.donut_options

        out["donut_options"] = aws_sdk_quicksight.types.donut_options.deserialize_json(
            data["DonutOptions"]
        )
    if "SmallMultiplesOptions" in data:
        import aws_sdk_quicksight.types.small_multiples_options

        out["small_multiples_options"] = (
            aws_sdk_quicksight.types.small_multiples_options.deserialize_json(
                data["SmallMultiplesOptions"]
            )
        )
    if "CategoryLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["category_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["CategoryLabelOptions"]
            )
        )
    if "ValueLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["value_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["ValueLabelOptions"]
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
