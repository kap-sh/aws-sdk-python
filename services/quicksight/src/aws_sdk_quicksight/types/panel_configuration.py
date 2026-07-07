"""Generated from Smithy shape ``com.amazonaws.quicksight#PanelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.hex_color_with_transparency
    import aws_sdk_quicksight.types.panel_border_style
    import aws_sdk_quicksight.types.panel_title_options
    import aws_sdk_quicksight.types.pixel_length
    import aws_sdk_quicksight.types.visibility


class PanelConfiguration(TypedDict, closed=True):
    title: NotRequired["aws_sdk_quicksight.types.panel_title_options.PanelTitleOptions"]
    """<p>Configures the title display within each small multiples panel.</p>"""
    border_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>Determines whether or not each panel displays a border.</p>"""
    border_thickness: NotRequired["aws_sdk_quicksight.types.pixel_length.PixelLength"]
    """<p>Sets the line thickness of panel borders.</p>"""
    border_style: NotRequired[
        "aws_sdk_quicksight.types.panel_border_style.PanelBorderStyle"
    ]
    """<p>Sets the line style of panel borders.</p>"""
    border_color: NotRequired[
        "aws_sdk_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>Sets the line color of panel borders.</p>"""
    gutter_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>Determines whether or not negative space between sibling panels is rendered.</p>"""
    gutter_spacing: NotRequired["aws_sdk_quicksight.types.pixel_length.PixelLength"]
    """<p>Sets the total amount of negative space to display between sibling panels.</p>"""
    background_visibility: NotRequired["aws_sdk_quicksight.types.visibility.Visibility"]
    """<p>Determines whether or not a background for each small multiples panel is rendered.</p>"""
    background_color: NotRequired[
        "aws_sdk_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>Sets the background color for each panel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PanelConfiguration) -> dict:
    out: dict = {}
    if "title" in value:
        import aws_sdk_quicksight.types.panel_title_options

        out["Title"] = aws_sdk_quicksight.types.panel_title_options.serialize_json(
            value["title"]
        )
    if "border_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["BorderVisibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["border_visibility"]
        )
    if "border_thickness" in value:
        out["BorderThickness"] = value["border_thickness"]
    if "border_style" in value:
        import aws_sdk_quicksight.types.panel_border_style

        out["BorderStyle"] = aws_sdk_quicksight.types.panel_border_style.serialize_json(
            value["border_style"]
        )
    if "border_color" in value:
        out["BorderColor"] = value["border_color"]
    if "gutter_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["GutterVisibility"] = aws_sdk_quicksight.types.visibility.serialize_json(
            value["gutter_visibility"]
        )
    if "gutter_spacing" in value:
        out["GutterSpacing"] = value["gutter_spacing"]
    if "background_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["BackgroundVisibility"] = (
            aws_sdk_quicksight.types.visibility.serialize_json(
                value["background_visibility"]
            )
        )
    if "background_color" in value:
        out["BackgroundColor"] = value["background_color"]
    return out


def deserialize_json(data: dict) -> PanelConfiguration:
    out: PanelConfiguration = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        import aws_sdk_quicksight.types.panel_title_options

        out["title"] = aws_sdk_quicksight.types.panel_title_options.deserialize_json(
            data["Title"]
        )
    if "BorderVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["border_visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["BorderVisibility"]
        )
    if "BorderThickness" in data:
        out["border_thickness"] = data["BorderThickness"]
    if "BorderStyle" in data:
        import aws_sdk_quicksight.types.panel_border_style

        out["border_style"] = (
            aws_sdk_quicksight.types.panel_border_style.deserialize_json(
                data["BorderStyle"]
            )
        )
    if "BorderColor" in data:
        out["border_color"] = data["BorderColor"]
    if "GutterVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["gutter_visibility"] = aws_sdk_quicksight.types.visibility.deserialize_json(
            data["GutterVisibility"]
        )
    if "GutterSpacing" in data:
        out["gutter_spacing"] = data["GutterSpacing"]
    if "BackgroundVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["background_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["BackgroundVisibility"]
            )
        )
    if "BackgroundColor" in data:
        out["background_color"] = data["BackgroundColor"]
    return out
