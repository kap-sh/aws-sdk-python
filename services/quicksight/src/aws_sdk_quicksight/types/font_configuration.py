"""Generated from Smithy shape ``com.amazonaws.quicksight#FontConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.font_decoration
    import aws_sdk_quicksight.types.font_size
    import aws_sdk_quicksight.types.font_style
    import aws_sdk_quicksight.types.font_weight
    import aws_sdk_quicksight.types.hex_color
    import aws_sdk_quicksight.types.limited_string


class FontConfiguration(TypedDict, closed=True):
    font_size: NotRequired["aws_sdk_quicksight.types.font_size.FontSize"]
    """<p>The option that determines the text display size.</p>"""
    font_decoration: NotRequired[
        "aws_sdk_quicksight.types.font_decoration.FontDecoration"
    ]
    """<p>Determines the appearance of decorative lines on the text.</p>"""
    font_color: NotRequired["aws_sdk_quicksight.types.hex_color.HexColor"]
    """<p>Determines the color of the text.</p>"""
    font_weight: NotRequired["aws_sdk_quicksight.types.font_weight.FontWeight"]
    """<p>The option that determines the text display weight, or boldness.</p>"""
    font_style: NotRequired["aws_sdk_quicksight.types.font_style.FontStyle"]
    """<p>Determines the text display face that is inherited by the given font family.</p>"""
    font_family: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The font family that you want to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FontConfiguration) -> dict:
    out: dict = {}
    if "font_size" in value:
        import aws_sdk_quicksight.types.font_size

        out["FontSize"] = aws_sdk_quicksight.types.font_size.serialize_json(
            value["font_size"]
        )
    if "font_decoration" in value:
        import aws_sdk_quicksight.types.font_decoration

        out["FontDecoration"] = aws_sdk_quicksight.types.font_decoration.serialize_json(
            value["font_decoration"]
        )
    if "font_color" in value:
        out["FontColor"] = value["font_color"]
    if "font_weight" in value:
        import aws_sdk_quicksight.types.font_weight

        out["FontWeight"] = aws_sdk_quicksight.types.font_weight.serialize_json(
            value["font_weight"]
        )
    if "font_style" in value:
        import aws_sdk_quicksight.types.font_style

        out["FontStyle"] = aws_sdk_quicksight.types.font_style.serialize_json(
            value["font_style"]
        )
    if "font_family" in value:
        out["FontFamily"] = value["font_family"]
    return out


def deserialize_json(data: dict) -> FontConfiguration:
    out: FontConfiguration = {}  # type: ignore[typeddict-item]
    if "FontSize" in data:
        import aws_sdk_quicksight.types.font_size

        out["font_size"] = aws_sdk_quicksight.types.font_size.deserialize_json(
            data["FontSize"]
        )
    if "FontDecoration" in data:
        import aws_sdk_quicksight.types.font_decoration

        out["font_decoration"] = (
            aws_sdk_quicksight.types.font_decoration.deserialize_json(
                data["FontDecoration"]
            )
        )
    if "FontColor" in data:
        out["font_color"] = data["FontColor"]
    if "FontWeight" in data:
        import aws_sdk_quicksight.types.font_weight

        out["font_weight"] = aws_sdk_quicksight.types.font_weight.deserialize_json(
            data["FontWeight"]
        )
    if "FontStyle" in data:
        import aws_sdk_quicksight.types.font_style

        out["font_style"] = aws_sdk_quicksight.types.font_style.deserialize_json(
            data["FontStyle"]
        )
    if "FontFamily" in data:
        out["font_family"] = data["FontFamily"]
    return out
