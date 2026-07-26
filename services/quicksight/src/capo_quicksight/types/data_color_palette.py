"""Generated from Smithy shape ``com.amazonaws.quicksight#DataColorPalette``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.color_list
    import capo_quicksight.types.hex_color


class DataColorPalette(TypedDict, closed=True):
    colors: NotRequired["capo_quicksight.types.color_list.ColorList"]
    """<p>The hexadecimal codes for the colors.</p>"""
    min_max_gradient: NotRequired["capo_quicksight.types.color_list.ColorList"]
    """<p>The minimum and maximum hexadecimal codes that describe a color gradient. </p>"""
    empty_fill_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The hexadecimal code of a color that applies to charts where a lack of data is highlighted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataColorPalette) -> dict:
    out: dict = {}
    if "colors" in value:
        import capo_quicksight.types.color_list

        out["Colors"] = capo_quicksight.types.color_list.serialize_json(value["colors"])
    if "min_max_gradient" in value:
        import capo_quicksight.types.color_list

        out["MinMaxGradient"] = capo_quicksight.types.color_list.serialize_json(
            value["min_max_gradient"]
        )
    if "empty_fill_color" in value:
        out["EmptyFillColor"] = value["empty_fill_color"]
    return out


def deserialize_json(data: dict) -> DataColorPalette:
    out: DataColorPalette = {}  # type: ignore[typeddict-item]
    if "Colors" in data:
        import capo_quicksight.types.color_list

        out["colors"] = capo_quicksight.types.color_list.deserialize_json(
            data["Colors"]
        )
    if "MinMaxGradient" in data:
        import capo_quicksight.types.color_list

        out["min_max_gradient"] = capo_quicksight.types.color_list.deserialize_json(
            data["MinMaxGradient"]
        )
    if "EmptyFillColor" in data:
        out["empty_fill_color"] = data["EmptyFillColor"]
    return out
