"""Generated from Smithy shape ``com.amazonaws.quicksight#TileLayoutStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.gutter_style
    import capo_quicksight.types.margin_style


class TileLayoutStyle(TypedDict, closed=True):
    gutter: NotRequired["capo_quicksight.types.gutter_style.GutterStyle"]
    """<p>The gutter settings that apply between tiles. </p>"""
    margin: NotRequired["capo_quicksight.types.margin_style.MarginStyle"]
    """<p>The margin settings that apply around the outside edge of sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TileLayoutStyle) -> dict:
    out: dict = {}
    if "gutter" in value:
        import capo_quicksight.types.gutter_style

        out["Gutter"] = capo_quicksight.types.gutter_style.serialize_json(
            value["gutter"]
        )
    if "margin" in value:
        import capo_quicksight.types.margin_style

        out["Margin"] = capo_quicksight.types.margin_style.serialize_json(
            value["margin"]
        )
    return out


def deserialize_json(data: dict) -> TileLayoutStyle:
    out: TileLayoutStyle = {}  # type: ignore[typeddict-item]
    if "Gutter" in data:
        import capo_quicksight.types.gutter_style

        out["gutter"] = capo_quicksight.types.gutter_style.deserialize_json(
            data["Gutter"]
        )
    if "Margin" in data:
        import capo_quicksight.types.margin_style

        out["margin"] = capo_quicksight.types.margin_style.deserialize_json(
            data["Margin"]
        )
    return out
