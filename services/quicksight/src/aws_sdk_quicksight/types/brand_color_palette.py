"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandColorPalette``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.palette


class BrandColorPalette(TypedDict, closed=True):
    primary: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    """<p>The primary color.</p>"""
    secondary: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    """<p>The secondary color.</p>"""
    accent: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    """<p>The color that is used for accent elements.</p>"""
    measure: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    """<p>The color that is used for measure elements.</p>"""
    dimension: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    """<p>The color that is used for dimension elements.</p>"""
    success: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    """<p>The color that is used for success elements.</p>"""
    info: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    """<p>The color that is used for info elements.</p>"""
    warning: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    """<p>The color that is used for warning elements.</p>"""
    danger: NotRequired["aws_sdk_quicksight.types.palette.Palette"]
    """<p>The color that is used for danger elements.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandColorPalette) -> dict:
    out: dict = {}
    if "primary" in value:
        import aws_sdk_quicksight.types.palette

        out["Primary"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["primary"]
        )
    if "secondary" in value:
        import aws_sdk_quicksight.types.palette

        out["Secondary"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["secondary"]
        )
    if "accent" in value:
        import aws_sdk_quicksight.types.palette

        out["Accent"] = aws_sdk_quicksight.types.palette.serialize_json(value["accent"])
    if "measure" in value:
        import aws_sdk_quicksight.types.palette

        out["Measure"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["measure"]
        )
    if "dimension" in value:
        import aws_sdk_quicksight.types.palette

        out["Dimension"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["dimension"]
        )
    if "success" in value:
        import aws_sdk_quicksight.types.palette

        out["Success"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["success"]
        )
    if "info" in value:
        import aws_sdk_quicksight.types.palette

        out["Info"] = aws_sdk_quicksight.types.palette.serialize_json(value["info"])
    if "warning" in value:
        import aws_sdk_quicksight.types.palette

        out["Warning"] = aws_sdk_quicksight.types.palette.serialize_json(
            value["warning"]
        )
    if "danger" in value:
        import aws_sdk_quicksight.types.palette

        out["Danger"] = aws_sdk_quicksight.types.palette.serialize_json(value["danger"])
    return out


def deserialize_json(data: dict) -> BrandColorPalette:
    out: BrandColorPalette = {}  # type: ignore[typeddict-item]
    if "Primary" in data:
        import aws_sdk_quicksight.types.palette

        out["primary"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Primary"]
        )
    if "Secondary" in data:
        import aws_sdk_quicksight.types.palette

        out["secondary"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Secondary"]
        )
    if "Accent" in data:
        import aws_sdk_quicksight.types.palette

        out["accent"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Accent"]
        )
    if "Measure" in data:
        import aws_sdk_quicksight.types.palette

        out["measure"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Measure"]
        )
    if "Dimension" in data:
        import aws_sdk_quicksight.types.palette

        out["dimension"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Dimension"]
        )
    if "Success" in data:
        import aws_sdk_quicksight.types.palette

        out["success"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Success"]
        )
    if "Info" in data:
        import aws_sdk_quicksight.types.palette

        out["info"] = aws_sdk_quicksight.types.palette.deserialize_json(data["Info"])
    if "Warning" in data:
        import aws_sdk_quicksight.types.palette

        out["warning"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Warning"]
        )
    if "Danger" in data:
        import aws_sdk_quicksight.types.palette

        out["danger"] = aws_sdk_quicksight.types.palette.deserialize_json(
            data["Danger"]
        )
    return out
