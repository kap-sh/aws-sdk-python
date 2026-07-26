"""Generated from Smithy shape ``com.amazonaws.quicksight#TableBorderOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.hex_color
    import capo_quicksight.types.table_border_style
    import capo_quicksight.types.table_border_thickness


class TableBorderOptions(TypedDict, closed=True):
    color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The color of a table border.</p>"""
    thickness: NotRequired[
        "capo_quicksight.types.table_border_thickness.TableBorderThickness"
    ]
    """<p>The thickness of a table border.</p>"""
    style: NotRequired["capo_quicksight.types.table_border_style.TableBorderStyle"]
    """<p>The style (none, solid) of a table border.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableBorderOptions) -> dict:
    out: dict = {}
    if "color" in value:
        out["Color"] = value["color"]
    if "thickness" in value:
        out["Thickness"] = value["thickness"]
    if "style" in value:
        import capo_quicksight.types.table_border_style

        out["Style"] = capo_quicksight.types.table_border_style.serialize_json(
            value["style"]
        )
    return out


def deserialize_json(data: dict) -> TableBorderOptions:
    out: TableBorderOptions = {}  # type: ignore[typeddict-item]
    if "Color" in data:
        out["color"] = data["Color"]
    if "Thickness" in data:
        out["thickness"] = data["Thickness"]
    if "Style" in data:
        import capo_quicksight.types.table_border_style

        out["style"] = capo_quicksight.types.table_border_style.deserialize_json(
            data["Style"]
        )
    return out
