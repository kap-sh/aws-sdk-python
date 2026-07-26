"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandColorPalette``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.palette


class BrandColorPalette(TypedDict, closed=True):
    primary: NotRequired["capo_quicksight.types.palette.Palette"]
    """<p>The primary color.</p>"""
    secondary: NotRequired["capo_quicksight.types.palette.Palette"]
    """<p>The secondary color.</p>"""
    accent: NotRequired["capo_quicksight.types.palette.Palette"]
    """<p>The color that is used for accent elements.</p>"""
    measure: NotRequired["capo_quicksight.types.palette.Palette"]
    """<p>The color that is used for measure elements.</p>"""
    dimension: NotRequired["capo_quicksight.types.palette.Palette"]
    """<p>The color that is used for dimension elements.</p>"""
    success: NotRequired["capo_quicksight.types.palette.Palette"]
    """<p>The color that is used for success elements.</p>"""
    info: NotRequired["capo_quicksight.types.palette.Palette"]
    """<p>The color that is used for info elements.</p>"""
    warning: NotRequired["capo_quicksight.types.palette.Palette"]
    """<p>The color that is used for warning elements.</p>"""
    danger: NotRequired["capo_quicksight.types.palette.Palette"]
    """<p>The color that is used for danger elements.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandColorPalette) -> dict:
    out: dict = {}
    if "primary" in value:
        import capo_quicksight.types.palette

        out["Primary"] = capo_quicksight.types.palette.serialize_json(value["primary"])
    if "secondary" in value:
        import capo_quicksight.types.palette

        out["Secondary"] = capo_quicksight.types.palette.serialize_json(
            value["secondary"]
        )
    if "accent" in value:
        import capo_quicksight.types.palette

        out["Accent"] = capo_quicksight.types.palette.serialize_json(value["accent"])
    if "measure" in value:
        import capo_quicksight.types.palette

        out["Measure"] = capo_quicksight.types.palette.serialize_json(value["measure"])
    if "dimension" in value:
        import capo_quicksight.types.palette

        out["Dimension"] = capo_quicksight.types.palette.serialize_json(
            value["dimension"]
        )
    if "success" in value:
        import capo_quicksight.types.palette

        out["Success"] = capo_quicksight.types.palette.serialize_json(value["success"])
    if "info" in value:
        import capo_quicksight.types.palette

        out["Info"] = capo_quicksight.types.palette.serialize_json(value["info"])
    if "warning" in value:
        import capo_quicksight.types.palette

        out["Warning"] = capo_quicksight.types.palette.serialize_json(value["warning"])
    if "danger" in value:
        import capo_quicksight.types.palette

        out["Danger"] = capo_quicksight.types.palette.serialize_json(value["danger"])
    return out


def deserialize_json(data: dict) -> BrandColorPalette:
    out: BrandColorPalette = {}  # type: ignore[typeddict-item]
    if "Primary" in data:
        import capo_quicksight.types.palette

        out["primary"] = capo_quicksight.types.palette.deserialize_json(data["Primary"])
    if "Secondary" in data:
        import capo_quicksight.types.palette

        out["secondary"] = capo_quicksight.types.palette.deserialize_json(
            data["Secondary"]
        )
    if "Accent" in data:
        import capo_quicksight.types.palette

        out["accent"] = capo_quicksight.types.palette.deserialize_json(data["Accent"])
    if "Measure" in data:
        import capo_quicksight.types.palette

        out["measure"] = capo_quicksight.types.palette.deserialize_json(data["Measure"])
    if "Dimension" in data:
        import capo_quicksight.types.palette

        out["dimension"] = capo_quicksight.types.palette.deserialize_json(
            data["Dimension"]
        )
    if "Success" in data:
        import capo_quicksight.types.palette

        out["success"] = capo_quicksight.types.palette.deserialize_json(data["Success"])
    if "Info" in data:
        import capo_quicksight.types.palette

        out["info"] = capo_quicksight.types.palette.deserialize_json(data["Info"])
    if "Warning" in data:
        import capo_quicksight.types.palette

        out["warning"] = capo_quicksight.types.palette.deserialize_json(data["Warning"])
    if "Danger" in data:
        import capo_quicksight.types.palette

        out["danger"] = capo_quicksight.types.palette.deserialize_json(data["Danger"])
    return out
