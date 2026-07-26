"""Generated from Smithy shape ``com.amazonaws.quicksight#FreeFormLayoutElementBackgroundStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.hex_color_with_transparency
    import capo_quicksight.types.visibility


class FreeFormLayoutElementBackgroundStyle(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The background visibility of a free-form layout element.</p>"""
    color: NotRequired[
        "capo_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>The background color of a free-form layout element.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeFormLayoutElementBackgroundStyle) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    if "color" in value:
        out["Color"] = value["color"]
    return out


def deserialize_json(data: dict) -> FreeFormLayoutElementBackgroundStyle:
    out: FreeFormLayoutElementBackgroundStyle = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "Color" in data:
        out["color"] = data["Color"]
    return out
