"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.axis_display_options
    import aws_sdk_quicksight.types.chart_axis_label_options
    import aws_sdk_quicksight.types.hex_color
    import aws_sdk_quicksight.types.legend_options
    import aws_sdk_quicksight.types.radar_chart_axes_range_scale
    import aws_sdk_quicksight.types.radar_chart_field_wells
    import aws_sdk_quicksight.types.radar_chart_series_settings
    import aws_sdk_quicksight.types.radar_chart_shape
    import aws_sdk_quicksight.types.radar_chart_sort_configuration
    import aws_sdk_quicksight.types.radar_chart_start_angle
    import aws_sdk_quicksight.types.visibility
    import aws_sdk_quicksight.types.visual_interaction_options
    import aws_sdk_quicksight.types.visual_palette


class RadarChartConfiguration(TypedDict):
    field_wells: NotRequired[
        "aws_sdk_quicksight.types.radar_chart_field_wells.RadarChartFieldWells"
    ]
    """<p>The field well configuration of a <code>RadarChartVisual</code>.</p>"""
    sort_configuration: NotRequired[
        "aws_sdk_quicksight.types.radar_chart_sort_configuration.RadarChartSortConfiguration"
    ]
    """<p>The sort configuration of a <code>RadarChartVisual</code>.</p>"""
    shape: NotRequired["aws_sdk_quicksight.types.radar_chart_shape.RadarChartShape"]
    """<p>The shape of the radar chart.</p>"""
    base_series_settings: NotRequired[
        "aws_sdk_quicksight.types.radar_chart_series_settings.RadarChartSeriesSettings"
    ]
    """<p>The base sreies settings of a radar chart.</p>"""
    start_angle: NotRequired[
        "aws_sdk_quicksight.types.radar_chart_start_angle.RadarChartStartAngle"
    ]
    """<p>The start angle of a radar chart's axis.</p>"""
    visual_palette: NotRequired["aws_sdk_quicksight.types.visual_palette.VisualPalette"]
    """<p>The palette (chart color) display setup of the visual.</p>"""
    alternate_band_colors_visibility: NotRequired[
        "aws_sdk_quicksight.types.visibility.Visibility"
    ]
    """<p>Determines the visibility of the colors of alternatign bands in a radar chart.</p>"""
    alternate_band_even_color: NotRequired[
        "aws_sdk_quicksight.types.hex_color.HexColor"
    ]
    """<p>The color of the even-numbered alternate bands of a radar chart.</p>"""
    alternate_band_odd_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>The color of the odd-numbered alternate bands of a radar chart.</p>"""
    category_axis: NotRequired[
        "aws_sdk_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The category axis of a radar chart.</p>"""
    category_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The category label options of a radar chart.</p>"""
    color_axis: NotRequired[
        "aws_sdk_quicksight.types.axis_display_options.AxisDisplayOptions"
    ]
    """<p>The color axis of a radar chart.</p>"""
    color_label_options: NotRequired[
        "aws_sdk_quicksight.types.chart_axis_label_options.ChartAxisLabelOptions"
    ]
    """<p>The color label options of a radar chart.</p>"""
    legend: NotRequired["aws_sdk_quicksight.types.legend_options.LegendOptions"]
    """<p>The legend display setup of the visual.</p>"""
    axes_range_scale: NotRequired[
        "aws_sdk_quicksight.types.radar_chart_axes_range_scale.RadarChartAxesRangeScale"
    ]
    """<p>The axis behavior options of a radar chart.</p>"""
    interactions: NotRequired[
        "aws_sdk_quicksight.types.visual_interaction_options.VisualInteractionOptions"
    ]
    """<p>The general visual interactions setup for a visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartConfiguration) -> dict:
    out: dict = {}
    if "field_wells" in value:
        import aws_sdk_quicksight.types.radar_chart_field_wells

        out["FieldWells"] = (
            aws_sdk_quicksight.types.radar_chart_field_wells.serialize_json(
                value["field_wells"]
            )
        )
    if "sort_configuration" in value:
        import aws_sdk_quicksight.types.radar_chart_sort_configuration

        out["SortConfiguration"] = (
            aws_sdk_quicksight.types.radar_chart_sort_configuration.serialize_json(
                value["sort_configuration"]
            )
        )
    if "shape" in value:
        import aws_sdk_quicksight.types.radar_chart_shape

        out["Shape"] = aws_sdk_quicksight.types.radar_chart_shape.serialize_json(
            value["shape"]
        )
    if "base_series_settings" in value:
        import aws_sdk_quicksight.types.radar_chart_series_settings

        out["BaseSeriesSettings"] = (
            aws_sdk_quicksight.types.radar_chart_series_settings.serialize_json(
                value["base_series_settings"]
            )
        )
    if "start_angle" in value:
        out["StartAngle"] = value["start_angle"]
    if "visual_palette" in value:
        import aws_sdk_quicksight.types.visual_palette

        out["VisualPalette"] = aws_sdk_quicksight.types.visual_palette.serialize_json(
            value["visual_palette"]
        )
    if "alternate_band_colors_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["AlternateBandColorsVisibility"] = (
            aws_sdk_quicksight.types.visibility.serialize_json(
                value["alternate_band_colors_visibility"]
            )
        )
    if "alternate_band_even_color" in value:
        out["AlternateBandEvenColor"] = value["alternate_band_even_color"]
    if "alternate_band_odd_color" in value:
        out["AlternateBandOddColor"] = value["alternate_band_odd_color"]
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
    if "color_axis" in value:
        import aws_sdk_quicksight.types.axis_display_options

        out["ColorAxis"] = aws_sdk_quicksight.types.axis_display_options.serialize_json(
            value["color_axis"]
        )
    if "color_label_options" in value:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["ColorLabelOptions"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.serialize_json(
                value["color_label_options"]
            )
        )
    if "legend" in value:
        import aws_sdk_quicksight.types.legend_options

        out["Legend"] = aws_sdk_quicksight.types.legend_options.serialize_json(
            value["legend"]
        )
    if "axes_range_scale" in value:
        import aws_sdk_quicksight.types.radar_chart_axes_range_scale

        out["AxesRangeScale"] = (
            aws_sdk_quicksight.types.radar_chart_axes_range_scale.serialize_json(
                value["axes_range_scale"]
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


def deserialize_json(data: dict) -> RadarChartConfiguration:
    out: RadarChartConfiguration = {}  # type: ignore[typeddict-item]
    if "FieldWells" in data:
        import aws_sdk_quicksight.types.radar_chart_field_wells

        out["field_wells"] = (
            aws_sdk_quicksight.types.radar_chart_field_wells.deserialize_json(
                data["FieldWells"]
            )
        )
    if "SortConfiguration" in data:
        import aws_sdk_quicksight.types.radar_chart_sort_configuration

        out["sort_configuration"] = (
            aws_sdk_quicksight.types.radar_chart_sort_configuration.deserialize_json(
                data["SortConfiguration"]
            )
        )
    if "Shape" in data:
        import aws_sdk_quicksight.types.radar_chart_shape

        out["shape"] = aws_sdk_quicksight.types.radar_chart_shape.deserialize_json(
            data["Shape"]
        )
    if "BaseSeriesSettings" in data:
        import aws_sdk_quicksight.types.radar_chart_series_settings

        out["base_series_settings"] = (
            aws_sdk_quicksight.types.radar_chart_series_settings.deserialize_json(
                data["BaseSeriesSettings"]
            )
        )
    if "StartAngle" in data:
        out["start_angle"] = data["StartAngle"]
    if "VisualPalette" in data:
        import aws_sdk_quicksight.types.visual_palette

        out["visual_palette"] = (
            aws_sdk_quicksight.types.visual_palette.deserialize_json(
                data["VisualPalette"]
            )
        )
    if "AlternateBandColorsVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["alternate_band_colors_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["AlternateBandColorsVisibility"]
            )
        )
    if "AlternateBandEvenColor" in data:
        out["alternate_band_even_color"] = data["AlternateBandEvenColor"]
    if "AlternateBandOddColor" in data:
        out["alternate_band_odd_color"] = data["AlternateBandOddColor"]
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
    if "ColorAxis" in data:
        import aws_sdk_quicksight.types.axis_display_options

        out["color_axis"] = (
            aws_sdk_quicksight.types.axis_display_options.deserialize_json(
                data["ColorAxis"]
            )
        )
    if "ColorLabelOptions" in data:
        import aws_sdk_quicksight.types.chart_axis_label_options

        out["color_label_options"] = (
            aws_sdk_quicksight.types.chart_axis_label_options.deserialize_json(
                data["ColorLabelOptions"]
            )
        )
    if "Legend" in data:
        import aws_sdk_quicksight.types.legend_options

        out["legend"] = aws_sdk_quicksight.types.legend_options.deserialize_json(
            data["Legend"]
        )
    if "AxesRangeScale" in data:
        import aws_sdk_quicksight.types.radar_chart_axes_range_scale

        out["axes_range_scale"] = (
            aws_sdk_quicksight.types.radar_chart_axes_range_scale.deserialize_json(
                data["AxesRangeScale"]
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
