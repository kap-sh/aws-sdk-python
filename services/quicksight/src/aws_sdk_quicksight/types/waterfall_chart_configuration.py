"""Generated from Smithy shape ``com.amazonaws.quicksight#WaterfallChartConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.axis_display_options
    import aws_sdk_quicksight.types.chart_axis_label_options
    import aws_sdk_quicksight.types.data_label_options
    import aws_sdk_quicksight.types.legend_options
    import aws_sdk_quicksight.types.visual_interaction_options
    import aws_sdk_quicksight.types.visual_palette
    import aws_sdk_quicksight.types.waterfall_chart_color_configuration
    import aws_sdk_quicksight.types.waterfall_chart_field_wells
    import aws_sdk_quicksight.types.waterfall_chart_options
    import aws_sdk_quicksight.types.waterfall_chart_sort_configuration


class WaterfallChartConfiguration(TypedDict):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.waterfall_chart_field_wells.WaterfallChartFieldWells"
    ]
    """<p>The field well configuration of a waterfall visual.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.waterfall_chart_sort_configuration.WaterfallChartSortConfiguration"
    ]
    """<p>The sort configuration of a waterfall visual.</p>"""
    waterfall_chart_options: NotRequired[
        "aws_sdk_quicksight.types.waterfall_chart_options.WaterfallChartOptions"
    ]
    """<p>The options that determine the presentation of a waterfall visual.</p>"""
    category_axis_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The options that determine the presentation of the category axis label.</p>"""
    category_axis_display_options: NotRequired[
        "aws_sdk_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the category axis.</p>"""
    primary_y_axis_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The options that determine the presentation of the y-axis label.</p>"""
    primary_y_axis_display_options: NotRequired[
        "aws_sdk_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The options that determine the presentation of the y-axis.</p>"""
    legend: NotRequired["aws_sdk_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend configuration of a waterfall visual.</p>"""
    data_labels: NotRequired[
        "aws_sdk_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The data label configuration of a waterfall visual.</p>"""
    visual_palette: NotRequired["aws_sdk_quicksight.types.visual_palette.VisualPalette"]
    """<p>The visual palette configuration of a waterfall visual.</p>"""
    color_configuration: NotRequired[
        "aws_sdk_quicksight.types.waterfall_chart_color_configuration.WaterfallChartColorConfiguration"
    ]
    """<p>The color configuration of a waterfall visual.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaterfallChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.waterfall_chart_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.waterfall_chart_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.waterfall_chart_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.waterfall_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "waterfall_chart_options" in value:
        import aws_sdk_quicksight.types.waterfall_chart_options

        out["WaterfallChartOptions"] = (
            aws_sdk_quicksight.types.waterfall_chart_options.serialize_json(
                value["waterfall_chart_options"]
            )
        )
    if "category_axis_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["CategoryAxisLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["category_axis_label_options"]
            )
        )
    if "category_axis_display_options" in value:
        import aws_sdk_quicksight.types.axis_display_options

        out["CategoryAxisDisplayOptions"] = (
            aws_sdk_quicksight.types.axis_display_options.serialize_json(
                value["category_axis_display_options"]
            )
        )
    if "primary_y_axis_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["PrimaryYAxisLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["primary_y_axis_label_options"]
            )
        )
    if "primary_y_axis_display_options" in value:
        import aws_sdk_quicksight.types.axis_display_options

        out["PrimaryYAxisDisplayOptions"] = (
            aws_sdk_quicksight.types.axis_display_options.serialize_json(
                value["primary_y_axis_display_options"]
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
    if "visual_palette" in value:
        import aws_sdk_quicksight.types.visual_palette

        out["VisualPalette"] = aws_sdk_quicksight.types.visual_palette.serialize_json(
            value["visual_palette"]
        )
    if "color_configuration" in value:
        import aws_sdk_quicksight.types.waterfall_chart_color_configuration

        out["ColorConfiguration"] = (
            aws_sdk_quicksight.types.waterfall_chart_color_configuration.serialize_json(
                value["color_configuration"]
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


def deserialize_json(data: dict) -> WaterfallChartConfiguration:
    out: WaterfallChartConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.waterfall_chart_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.waterfall_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.waterfall_chart_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.waterfall_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if "WaterfallChartOptions" in data:
        import aws_sdk_quicksight.types.waterfall_chart_options

        out["waterfall_chart_options"] = (
            aws_sdk_quicksight.types.waterfall_chart_options.deserialize_json(
                data["WaterfallChartOptions"]
            )
        )
    if "CategoryAxisLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["category_axis_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["CategoryAxisLabelOptions"]
            )
        )
    if "CategoryAxisDisplayOptions" in data:
        import aws_sdk_quicksight.types.axis_display_options

        out["category_axis_display_options"] = (
            aws_sdk_quicksight.types.axis_display_options.deserialize_json(
                data["CategoryAxisDisplayOptions"]
            )
        )
    if "PrimaryYAxisLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["primary_y_axis_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["PrimaryYAxisLabelOptions"]
            )
        )
    if "PrimaryYAxisDisplayOptions" in data:
        import aws_sdk_quicksight.types.axis_display_options

        out["primary_y_axis_display_options"] = (
            aws_sdk_quicksight.types.axis_display_options.deserialize_json(
                data["PrimaryYAxisDisplayOptions"]
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
    if "VisualPalette" in data:
        import aws_sdk_quicksight.types.visual_palette

        out["visual_palette"] = (
            aws_sdk_quicksight.types.visual_palette.deserialize_json(
                data["VisualPalette"]
            )
        )
    if "ColorConfiguration" in data:
        import aws_sdk_quicksight.types.waterfall_chart_color_configuration

        out["color_configuration"] = (
            aws_sdk_quicksight.types.waterfall_chart_color_configuration.deserialize_json(
                data["ColorConfiguration"]
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
