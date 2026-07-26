"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLineStyle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_line_symbol_style


class GeospatialLineStyle(TypedDict, closed=True):
    line_symbol_style: NotRequired[
        "capo_quicksight.types.geospatial_line_symbol_style.GeospatialLineSymbolStyle"
    ]
    """<p>The symbol style for a line style.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLineStyle) -> dict:
    out: dict = {}
    if "line_symbol_style" in value:
        import capo_quicksight.types.geospatial_line_symbol_style

        out["LineSymbolStyle"] = (
            capo_quicksight.types.geospatial_line_symbol_style.serialize_json(
                value["line_symbol_style"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialLineStyle:
    out: GeospatialLineStyle = {}  # type: ignore[typeddict-item]
    if "LineSymbolStyle" in data:
        import capo_quicksight.types.geospatial_line_symbol_style

        out["line_symbol_style"] = (
            capo_quicksight.types.geospatial_line_symbol_style.deserialize_json(
                data["LineSymbolStyle"]
            )
        )
    return out
