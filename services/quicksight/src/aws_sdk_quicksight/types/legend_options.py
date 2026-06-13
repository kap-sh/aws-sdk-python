"""Generated from Smithy shape ``com.amazonaws.quicksight#LegendOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.font_configuration
    import aws_sdk_quicksight.types.label_options
    import aws_sdk_quicksight.types.legend_position
    import aws_sdk_quicksight.types.pixel_length
    import aws_sdk_quicksight.types.visibility


class LegendOptions(TypedDict):
    visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>Determines whether or not the legend is visible.</p>"""
    title: NotRequired["aws_sdk_quicksight.types.label_options.LabelOptions"]
    """<p>The custom title for the legend.</p>"""
    position: NotRequired["aws_sdk_quicksight.types.legend_position.LegendPosition"]
    """<p>The positions for the legend. Choose one of the following options:</p> <ul> <li> <p> <code>AUTO</code> </p> </li> <li> <p> <code>RIGHT</code> </p> </li> <li> <p> <code>BOTTOM</code> </p> </li> <li> <p> <code>LEFT</code> </p> </li> </ul>"""
    width: NotRequired["aws_sdk_quicksight.types.pixel_length.PixelLength"]
    """<p>The width of the legend. If this value is omitted, a default width is used when rendering.</p>"""
    height: NotRequired["aws_sdk_quicksight.types.pixel_length.PixelLength"]
    """<p>The height of the legend. If this value is omitted, a default height is used when rendering.</p>"""
    value_font_configuration: NotRequired[
        "aws_sdk_quicksight.types.font_configuration.FontConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: LegendOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["Visibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "title" in value:
        import aws_sdk_quicksight.types.label_options

        out["Title"] = aws_sdk_quicksight.types.label_options.serialize_json(
            value["title"]
        )
    if "position" in value:
        import aws_sdk_quicksight.types.legend_position

        out["Position"] = aws_sdk_quicksight.types.legend_position.serialize_json(
            value["position"]
        )
    if "width" in value:
        out["Width"] = value["width"]
    if "height" in value:
        out["Height"] = value["height"]
    if "value_font_configuration" in value:
        import aws_sdk_quicksight.types.font_configuration

        out["ValueFontConfiguration"] = (
            aws_sdk_quicksight.types.font_configuration.serialize_json(
                value["value_font_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> LegendOptions:
    out: LegendOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "Title" in data:
        import aws_sdk_quicksight.types.label_options

        out["title"] = aws_sdk_quicksight.types.label_options.deserialize_json(
            data["Title"]
        )
    if "Position" in data:
        import aws_sdk_quicksight.types.legend_position

        out["position"] = aws_sdk_quicksight.types.legend_position.deserialize_json(
            data["Position"]
        )
    if "Width" in data:
        out["width"] = data["Width"]
    if "Height" in data:
        out["height"] = data["Height"]
    if "ValueFontConfiguration" in data:
        import aws_sdk_quicksight.types.font_configuration

        out["value_font_configuration"] = (
            aws_sdk_quicksight.types.font_configuration.deserialize_json(
                data["ValueFontConfiguration"]
            )
        )
    return out
