"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.chart_axis_label_options
    import aws_sdk_quicksight.types.funnel_chart_data_label_options
    import aws_sdk_quicksight.types.funnel_chart_field_wells
    import aws_sdk_quicksight.types.funnel_chart_sort_configuration
    import aws_sdk_quicksight.types.tooltip_options
    import aws_sdk_quicksight.types.visual_interaction_options
    import aws_sdk_quicksight.types.visual_palette


class FunnelChartConfiguration(TypedDict):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.funnel_chart_field_wells.FunnelChartFieldWells"
    ]
    """<p>The field well configuration of a <code>FunnelChartVisual</code>.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.funnel_chart_sort_configuration.FunnelChartSortConfiguration"
    ]
    """<p>The sort configuration of a <code>FunnelChartVisual</code>.</p>"""
    category_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options of the categories that are displayed in a <code>FunnelChartVisual</code>.</p>"""
    value_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The label options for the values that are displayed in a <code>FunnelChartVisual</code>.</p>"""
    tooltip: NotRequired["aws_sdk_quicksight.types.tooltip_options.TooltipOptions"]
    """<p>The tooltip configuration of a <code>FunnelChartVisual</code>.</p>"""
    data_label_options: NotRequired[
        "aws_sdk_quicksight.types.funnel_chart_data_label_options.FunnelChartDataLabelOptions"
    ]
    """<p>The options that determine the presentation of the data labels.</p>"""
    visual_palette: NotRequired["aws_sdk_quicksight.types.visual_palette.VisualPalette"]
    """<p>The visual palette configuration of a <code>FunnelChartVisual</code>.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunnelChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.funnel_chart_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.funnel_chart_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.funnel_chart_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.funnel_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
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
    if "tooltip" in value:
        import aws_sdk_quicksight.types.tooltip_options

        out["Tooltip"] = aws_sdk_quicksight.types.tooltip_options.serialize_json(
            value["tooltip"]
        )
    if "data_label_options" in value:
        import aws_sdk_quicksight.types.funnel_chart_data_label_options

        out["DataLabelOptions"] = (
            aws_sdk_quicksight.types.funnel_chart_data_label_options.serialize_json(
                value["data_label_options"]
            )
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


def deserialize_json(data: dict) -> FunnelChartConfiguration:
    out: FunnelChartConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.funnel_chart_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.funnel_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.funnel_chart_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.funnel_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
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
    if "Tooltip" in data:
        import aws_sdk_quicksight.types.tooltip_options

        out["tooltip"] = aws_sdk_quicksight.types.tooltip_options.deserialize_json(
            data["Tooltip"]
        )
    if "DataLabelOptions" in data:
        import aws_sdk_quicksight.types.funnel_chart_data_label_options

        out["data_label_options"] = (
            aws_sdk_quicksight.types.funnel_chart_data_label_options.deserialize_json(
                data["DataLabelOptions"]
            )
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
