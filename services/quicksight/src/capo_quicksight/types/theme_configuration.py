"""Generated from Smithy shape ``com.amazonaws.quicksight#ThemeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_color_palette
    import capo_quicksight.types.sheet_style
    import capo_quicksight.types.typography
    import capo_quicksight.types.ui_color_palette


class ThemeConfiguration(TypedDict, closed=True):
    data_color_palette: NotRequired[
        "capo_quicksight.types.data_color_palette.DataColorPalette"
    ]
    """<p>Color properties that apply to chart data colors.</p>"""
    ui_color_palette: NotRequired[
        "capo_quicksight.types.ui_color_palette.UIColorPalette"
    ]
    """<p>Color properties that apply to the UI and to charts, excluding the colors that apply to data. </p>"""
    sheet: NotRequired["capo_quicksight.types.sheet_style.SheetStyle"]
    """<p>Display options related to sheets.</p>"""
    typography: NotRequired["capo_quicksight.types.typography.Typography"]


# --- restJson1 ser/de ---
def serialize_json(value: ThemeConfiguration) -> dict:
    out: dict = {}
    if "data_color_palette" in value:
        import capo_quicksight.types.data_color_palette

        out["DataColorPalette"] = (
            capo_quicksight.types.data_color_palette.serialize_json(
                value["data_color_palette"]
            )
        )
    if "ui_color_palette" in value:
        import capo_quicksight.types.ui_color_palette

        out["UIColorPalette"] = capo_quicksight.types.ui_color_palette.serialize_json(
            value["ui_color_palette"]
        )
    if "sheet" in value:
        import capo_quicksight.types.sheet_style

        out["Sheet"] = capo_quicksight.types.sheet_style.serialize_json(value["sheet"])
    if "typography" in value:
        import capo_quicksight.types.typography

        out["Typography"] = capo_quicksight.types.typography.serialize_json(
            value["typography"]
        )
    return out


def deserialize_json(data: dict) -> ThemeConfiguration:
    out: ThemeConfiguration = {}  # type: ignore[typeddict-item]
    if "DataColorPalette" in data:
        import capo_quicksight.types.data_color_palette

        out["data_color_palette"] = (
            capo_quicksight.types.data_color_palette.deserialize_json(
                data["DataColorPalette"]
            )
        )
    if "UIColorPalette" in data:
        import capo_quicksight.types.ui_color_palette

        out["ui_color_palette"] = (
            capo_quicksight.types.ui_color_palette.deserialize_json(
                data["UIColorPalette"]
            )
        )
    if "Sheet" in data:
        import capo_quicksight.types.sheet_style

        out["sheet"] = capo_quicksight.types.sheet_style.deserialize_json(data["Sheet"])
    if "Typography" in data:
        import capo_quicksight.types.typography

        out["typography"] = capo_quicksight.types.typography.deserialize_json(
            data["Typography"]
        )
    return out
