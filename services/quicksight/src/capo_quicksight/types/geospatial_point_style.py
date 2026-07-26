"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialPointStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_circle_symbol_style


class GeospatialPointStyle(TypedDict, closed=True):
    circle_symbol_style: NotRequired[
        "capo_quicksight.types.geospatial_circle_symbol_style.GeospatialCircleSymbolStyle"
    ]
    """<p>The circle symbol style for a point layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialPointStyle) -> dict:
    out: dict = {}
    if "circle_symbol_style" in value:
        import capo_quicksight.types.geospatial_circle_symbol_style

        out["CircleSymbolStyle"] = (
            capo_quicksight.types.geospatial_circle_symbol_style.serialize_json(
                value["circle_symbol_style"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialPointStyle:
    out: GeospatialPointStyle = {}  # type: ignore[typeddict-item]
    if "CircleSymbolStyle" in data:
        import capo_quicksight.types.geospatial_circle_symbol_style

        out["circle_symbol_style"] = (
            capo_quicksight.types.geospatial_circle_symbol_style.deserialize_json(
                data["CircleSymbolStyle"]
            )
        )
    return out
