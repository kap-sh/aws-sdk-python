"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialPointLayer``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_point_style


class GeospatialPointLayer(TypedDict, closed=True):
    style: "capo_quicksight.types.geospatial_point_style.GeospatialPointStyle"
    """<p>The visualization style for a point layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialPointLayer) -> dict:
    out: dict = {}
    import capo_quicksight.types.geospatial_point_style

    out["Style"] = capo_quicksight.types.geospatial_point_style.serialize_json(
        value["style"]
    )
    return out


def deserialize_json(data: dict) -> GeospatialPointLayer:
    out: GeospatialPointLayer = {}  # type: ignore[typeddict-item]
    if "Style" in data:
        import capo_quicksight.types.geospatial_point_style

        out["style"] = capo_quicksight.types.geospatial_point_style.deserialize_json(
            data["Style"]
        )
    else:
        raise DeserializationError("GeospatialPointLayer.style required")
    return out
