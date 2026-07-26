"""Generated from Smithy shape ``com.amazonaws.quicksight#FunnelChartDataLabelOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_label_position
    import capo_quicksight.types.font_configuration
    import capo_quicksight.types.funnel_chart_measure_data_label_style
    import capo_quicksight.types.hex_color
    import capo_quicksight.types.visibility


class FunnelChartDataLabelOptions(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility option that determines if data labels are displayed.</p>"""
    category_label_visibility: NotRequired[
        "capo_quicksight.types.visibility.Visibility"
    ]
    """<p>The visibility of the category labels within the data labels.</p>"""
    measure_label_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the measure labels within the data labels.</p>"""
    position: NotRequired["capo_quicksight.types.data_label_position.DataLabelPosition"]
    """<p>Determines the positioning of the data label relative to a section of the funnel.</p>"""
    label_font_configuration: NotRequired[
        "capo_quicksight.types.font_configuration.FontConfiguration"
    ]
    """<p>The font configuration for the data labels.</p> <p>Only the <code>FontSize</code> attribute of the font configuration is used for data labels.</p>"""
    label_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The color of the data label text.</p>"""
    measure_data_label_style: NotRequired[
        "capo_quicksight.types.funnel_chart_measure_data_label_style.FunnelChartMeasureDataLabelStyle"
    ]
    """<p>Determines the style of the metric labels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunnelChartDataLabelOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "category_label_visibility" in value:
        import capo_quicksight.types.visibility

        out["CategoryLabelVisibility"] = (
            capo_quicksight.types.visibility.serialize_json(
                value["category_label_visibility"]
            )
        )
    if "measure_label_visibility" in value:
        import capo_quicksight.types.visibility

        out["MeasureLabelVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["measure_label_visibility"]
        )
    if "position" in value:
        import capo_quicksight.types.data_label_position

        out["Position"] = capo_quicksight.types.data_label_position.serialize_json(
            value["position"]
        )
    if "label_font_configuration" in value:
        import capo_quicksight.types.font_configuration

        out["LabelFontConfiguration"] = (
            capo_quicksight.types.font_configuration.serialize_json(
                value["label_font_configuration"]
            )
        )
    if "label_color" in value:
        out["LabelColor"] = value["label_color"]
    if "measure_data_label_style" in value:
        import capo_quicksight.types.funnel_chart_measure_data_label_style

        out["MeasureDataLabelStyle"] = (
            capo_quicksight.types.funnel_chart_measure_data_label_style.serialize_json(
                value["measure_data_label_style"]
            )
        )
    return out


def deserialize_json(data: dict) -> FunnelChartDataLabelOptions:
    out: FunnelChartDataLabelOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "CategoryLabelVisibility" in data:
        import capo_quicksight.types.visibility

        out["category_label_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["CategoryLabelVisibility"]
            )
        )
    if "MeasureLabelVisibility" in data:
        import capo_quicksight.types.visibility

        out["measure_label_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["MeasureLabelVisibility"]
            )
        )
    if "Position" in data:
        import capo_quicksight.types.data_label_position

        out["position"] = capo_quicksight.types.data_label_position.deserialize_json(
            data["Position"]
        )
    if "LabelFontConfiguration" in data:
        import capo_quicksight.types.font_configuration

        out["label_font_configuration"] = (
            capo_quicksight.types.font_configuration.deserialize_json(
                data["LabelFontConfiguration"]
            )
        )
    if "LabelColor" in data:
        out["label_color"] = data["LabelColor"]
    if "MeasureDataLabelStyle" in data:
        import capo_quicksight.types.funnel_chart_measure_data_label_style

        out["measure_data_label_style"] = (
            capo_quicksight.types.funnel_chart_measure_data_label_style.deserialize_json(
                data["MeasureDataLabelStyle"]
            )
        )
    return out
