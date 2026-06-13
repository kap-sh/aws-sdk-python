"""Generated from Smithy shape ``com.amazonaws.quicksight#ApplicationTheme``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.brand_color_palette
    import aws_sdk_quicksight.types.brand_element_style
    import aws_sdk_quicksight.types.contextual_accent_palette


class ApplicationTheme(TypedDict):
    brand_color_palette: NotRequired[
        "aws_sdk_quicksight.types.brand_color_palette.BrandColorPalette"
    ]
    """<p>The color palette.</p>"""
    contextual_accent_palette: NotRequired[
        "aws_sdk_quicksight.types.contextual_accent_palette.ContextualAccentPalette"
    ]
    """<p>The contextual accent palette.</p>"""
    brand_element_style: NotRequired[
        "aws_sdk_quicksight.types.brand_element_style.BrandElementStyle"
    ]
    """<p>The element style.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationTheme) -> dict:
    out: dict = {}
    if "brand_color_palette" in value:
        import aws_sdk_quicksight.types.brand_color_palette

        out["BrandColorPalette"] = (
            aws_sdk_quicksight.types.brand_color_palette.serialize_json(
                value["brand_color_palette"]
            )
        )
    if "contextual_accent_palette" in value:
        import aws_sdk_quicksight.types.contextual_accent_palette

        out["ContextualAccentPalette"] = (
            aws_sdk_quicksight.types.contextual_accent_palette.serialize_json(
                value["contextual_accent_palette"]
            )
        )
    if "brand_element_style" in value:
        import aws_sdk_quicksight.types.brand_element_style

        out["BrandElementStyle"] = (
            aws_sdk_quicksight.types.brand_element_style.serialize_json(
                value["brand_element_style"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplicationTheme:
    out: ApplicationTheme = {}  # type: ignore[typeddict-item]
    if "BrandColorPalette" in data:
        import aws_sdk_quicksight.types.brand_color_palette

        out["brand_color_palette"] = (
            aws_sdk_quicksight.types.brand_color_palette.deserialize_json(
                data["BrandColorPalette"]
            )
        )
    if "ContextualAccentPalette" in data:
        import aws_sdk_quicksight.types.contextual_accent_palette

        out["contextual_accent_palette"] = (
            aws_sdk_quicksight.types.contextual_accent_palette.deserialize_json(
                data["ContextualAccentPalette"]
            )
        )
    if "BrandElementStyle" in data:
        import aws_sdk_quicksight.types.brand_element_style

        out["brand_element_style"] = (
            aws_sdk_quicksight.types.brand_element_style.deserialize_json(
                data["BrandElementStyle"]
            )
        )
    return out
