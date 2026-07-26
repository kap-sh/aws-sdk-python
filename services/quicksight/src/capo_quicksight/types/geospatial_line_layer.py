"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialLineLayer``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_line_style


class GeospatialLineLayer(TypedDict, closed=True):
    style: "capo_quicksight.types.geospatial_line_style.GeospatialLineStyle"
    """<p>The visualization style for a line layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialLineLayer) -> dict:
    out: dict = {}
    import capo_quicksight.types.geospatial_line_style

    out["Style"] = capo_quicksight.types.geospatial_line_style.serialize_json(
        value["style"]
    )
    return out


def deserialize_json(data: dict) -> GeospatialLineLayer:
    out: GeospatialLineLayer = {}  # type: ignore[typeddict-item]
    if "Style" in data:
        import capo_quicksight.types.geospatial_line_style

        out["style"] = capo_quicksight.types.geospatial_line_style.deserialize_json(
            data["Style"]
        )
    else:
        raise DeserializationError("GeospatialLineLayer.style required")
    return out
