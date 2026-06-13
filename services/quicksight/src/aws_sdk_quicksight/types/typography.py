"""Generated from Smithy shape ``com.amazonaws.quicksight#Typography``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.control_title_font_configuration
    import aws_sdk_quicksight.types.font_configuration
    import aws_sdk_quicksight.types.font_list
    import aws_sdk_quicksight.types.visual_subtitle_font_configuration
    import aws_sdk_quicksight.types.visual_title_font_configuration


class Typography(TypedDict):
    font_families: NotRequired["aws_sdk_quicksight.types.font_list.FontList"]
    """<p>Determines the list of font families.</p>"""
    axis_title_font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    axis_label_font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    legend_title_font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    legend_value_font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    data_label_font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]
    visual_title_font_configuration: NotRequired[
        "aws_sdk_quicksight.types.visual_title_font_configuration.VisualTitleFontConfiguration"
    ]
    """<p>Configures the display properties of the visual title.</p>"""
    visual_subtitle_font_configuration: NotRequired[
        "aws_sdk_quicksight.types.visual_subtitle_font_configuration.VisualSubtitleFontConfiguration"
    ]
    """<p>Configures the display properties of the visual sub-title.</p>"""
    control_title_font_configuration: NotRequired[
        "aws_sdk_quicksight.types.control_title_font_configuration.ControlTitleFontConfiguration"
    ]
    """<p>Configures the display properties of the control title.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Typography) -> dict:
    out: dict = {}
    if "font_families" in value:
        import aws_sdk_quicksight.types.font_list

        out["FontFamilies"] = aws_sdk_quicksight.types.font_list.serialize_json(
            value["font_families"]
        )
    if "axis_title_font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["AxisTitleFontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["axis_title_font_configuration"]
            )
        )
    if "axis_label_font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["AxisLabelFontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["axis_label_font_configuration"]
            )
        )
    if "legend_title_font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["LegendTitleFontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["legend_title_font_configuration"]
            )
        )
    if "legend_value_font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["LegendValueFontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["legend_value_font_configuration"]
            )
        )
    if "data_label_font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["DataLabelFontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["data_label_font_configuration"]
            )
        )
    if "visual_title_font_configuration" in value:
        import aws_sdk_quicksight.types.visual_title_font_configuration

        out["VisualTitleFontConfiguration"] = (
            aws_sdk_quicksight.types.visual_title_font_configuration.serialize_json(
                value["visual_title_font_configuration"]
            )
        )
    if "visual_subtitle_font_configuration" in value:
        import aws_sdk_quicksight.types.visual_subtitle_font_configuration

        out["VisualSubtitleFontConfiguration"] = (
            aws_sdk_quicksight.types.visual_subtitle_font_configuration.serialize_json(
                value["visual_subtitle_font_configuration"]
            )
        )
    if "control_title_font_configuration" in value:
        import aws_sdk_quicksight.types.control_title_font_configuration

        out["ControlTitleFontConfiguration"] = (
            aws_sdk_quicksight.types.control_title_font_configuration.serialize_json(
                value["control_title_font_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Typography:
    out: Typography = {}  # type: ignore[typeddict-item]
    if "FontFamilies" in data:
        import aws_sdk_quicksight.types.font_list

        out["font_families"] = aws_sdk_quicksight.types.font_list.deserialize_json(
            data["FontFamilies"]
        )
    if "AxisTitleFontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["axis_title_font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["AxisTitleFontConfiguration"]
            )
        )
    if "AxisLabelFontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["axis_label_font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["AxisLabelFontConfiguration"]
            )
        )
    if "LegendTitleFontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["legend_title_font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["LegendTitleFontConfiguration"]
            )
        )
    if "LegendValueFontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["legend_value_font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["LegendValueFontConfiguration"]
            )
        )
    if "DataLabelFontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["data_label_font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["DataLabelFontConfiguration"]
            )
        )
    if "VisualTitleFontConfiguration" in data:
        import aws_sdk_quicksight.types.visual_title_font_configuration

        out["visual_title_font_configuration"] = (
            aws_sdk_quicksight.types.visual_title_font_configuration.deserialize_json(
                data["VisualTitleFontConfiguration"]
            )
        )
    if "VisualSubtitleFontConfiguration" in data:
        import aws_sdk_quicksight.types.visual_subtitle_font_configuration

        out["visual_subtitle_font_configuration"] = (
            aws_sdk_quicksight.types.visual_subtitle_font_configuration.deserialize_json(
                data["VisualSubtitleFontConfiguration"]
            )
        )
    if "ControlTitleFontConfiguration" in data:
        import aws_sdk_quicksight.types.control_title_font_configuration

        out["control_title_font_configuration"] = (
            aws_sdk_quicksight.types.control_title_font_configuration.deserialize_json(
                data["ControlTitleFontConfiguration"]
            )
        )
    return out
