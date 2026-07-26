"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialMapStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.base_map_style_type
    import capo_quicksight.types.hex_color_with_transparency
    import capo_quicksight.types.visibility


class GeospatialMapStyle(TypedDict, closed=True):
    base_map_style: NotRequired[
        "capo_quicksight.types.base_map_style_type.BaseMapStyleType"
    ]
    """<p>The selected base map style.</p>"""
    background_color: NotRequired[
        "capo_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>The background color and opacity values for a map.</p>"""
    base_map_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The state of visibility for the base map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialMapStyle) -> dict:
    out: dict = {}
    if "base_map_style" in value:
        import capo_quicksight.types.base_map_style_type

        out["BaseMapStyle"] = capo_quicksight.types.base_map_style_type.serialize_json(
            value["base_map_style"]
        )
    if "background_color" in value:
        out["BackgroundColor"] = value["background_color"]
    if "base_map_visibility" in value:
        import capo_quicksight.types.visibility

        out["BaseMapVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["base_map_visibility"]
        )
    return out


def deserialize_json(data: dict) -> GeospatialMapStyle:
    out: GeospatialMapStyle = {}  # type: ignore[typeddict-item]
    if "BaseMapStyle" in data:
        import capo_quicksight.types.base_map_style_type

        out["base_map_style"] = (
            capo_quicksight.types.base_map_style_type.deserialize_json(
                data["BaseMapStyle"]
            )
        )
    if "BackgroundColor" in data:
        out["background_color"] = data["BackgroundColor"]
    if "BaseMapVisibility" in data:
        import capo_quicksight.types.visibility

        out["base_map_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["BaseMapVisibility"]
        )
    return out
