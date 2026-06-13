"""Generated from Smithy shape ``com.amazonaws.quicksight#GaugeChartConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_label_options
    import aws_sdk_quicksight.types.gauge_chart_color_configuration
    import aws_sdk_quicksight.types.gauge_chart_field_wells
    import aws_sdk_quicksight.types.gauge_chart_options
    import aws_sdk_quicksight.types.tooltip_options
    import aws_sdk_quicksight.types.visual_interaction_options
    import aws_sdk_quicksight.types.visual_palette


class GaugeChartConfiguration(TypedDict):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.gauge_chart_field_wells.GaugeChartFieldWells"
    ]
    """<p>The field well configuration of a <code>GaugeChartVisual</code>.</p>"""
    gauge_chart_options: NotRequired[
        "aws_sdk_quicksight.types.gauge_chart_options.GaugeChartOptions"
    ]
    """<p>The options that determine the presentation of the <code>GaugeChartVisual</code>.</p>"""
    data_labels: NotRequired[
        "aws_sdk_quicksight.types.data_label_options.DataLabelOptions"
    ]
    """<p>The data label configuration of a <code>GaugeChartVisual</code>.</p>"""
    tooltip_options: NotRequired[
        "aws_sdk_quicksight.types.tooltip_options.TooltipOptions"
    ]
    """<p>The tooltip configuration of a <code>GaugeChartVisual</code>.</p>"""
    visual_palette: NotRequired["aws_sdk_quicksight.types.visual_palette.VisualPalette"]
    """<p>The visual palette configuration of a <code>GaugeChartVisual</code>.</p>"""
    color_configuration: NotRequired[
        "aws_sdk_quicksight.types.gauge_chart_color_configuration.GaugeChartColorConfiguration"
    ]
    """<p>The color configuration of a <code>GaugeChartVisual</code>.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GaugeChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.gauge_chart_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.gauge_chart_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "gauge_chart_options" in value:
        import aws_sdk_quicksight.types.gauge_chart_options

        out["GaugeChartOptions"] = (
            aws_sdk_quicksight.types.gauge_chart_options.serialize_json(
                value["gauge_chart_options"]
            )
        )
    if "data_labels" in value:
        import aws_sdk_quicksight.types.data_label_options

        out["DataLabels"] = aws_sdk_quicksight.types.data_label_options.serialize_json(
            value["data_labels"]
        )
    if "tooltip_options" in value:
        import aws_sdk_quicksight.types.tooltip_options

        out["TooltipOptions"] = aws_sdk_quicksight.types.tooltip_options.serialize_json(
            value["tooltip_options"]
        )
    if "visual_palette" in value:
        import aws_sdk_quicksight.types.visual_palette

        out["VisualPalette"] = aws_sdk_quicksight.types.visual_palette.serialize_json(
            value["visual_palette"]
        )
    if "color_configuration" in value:
        import aws_sdk_quicksight.types.gauge_chart_color_configuration

        out["ColorConfiguration"] = (
            aws_sdk_quicksight.types.gauge_chart_color_configuration.serialize_json(
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


def deserialize_json(data: dict) -> GaugeChartConfiguration:
    out: GaugeChartConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.gauge_chart_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.gauge_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "GaugeChartOptions" in data:
        import aws_sdk_quicksight.types.gauge_chart_options

        out["gauge_chart_options"] = (
            aws_sdk_quicksight.types.gauge_chart_options.deserialize_json(
                data["GaugeChartOptions"]
            )
        )
    if "DataLabels" in data:
        import aws_sdk_quicksight.types.data_label_options

        out["data_labels"] = (
            aws_sdk_quicksight.types.data_label_options.deserialize_json(
                data["DataLabels"]
            )
        )
    if "TooltipOptions" in data:
        import aws_sdk_quicksight.types.tooltip_options

        out["tooltip_options"] = (
            aws_sdk_quicksight.types.tooltip_options.deserialize_json(
                data["TooltipOptions"]
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
        import aws_sdk_quicksight.types.gauge_chart_color_configuration

        out["color_configuration"] = (
            aws_sdk_quicksight.types.gauge_chart_color_configuration.deserialize_json(
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
