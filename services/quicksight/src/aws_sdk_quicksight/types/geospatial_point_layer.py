"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialPointLayer``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_point_style


class GeospatialPointLayer(TypedDict):
    style: "aws_sdk_quicksight.types.geospatial_point_style.GeospatialPointStyle"
    """<p>The visualization style for a point layer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialPointLayer) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.geospatial_point_style

    out["Style"] = aws_sdk_quicksight.types.geospatial_point_style.serialize_json(
        value["style"]
    )
    return out


def deserialize_json(data: dict) -> GeospatialPointLayer:
    out: GeospatialPointLayer = {}  # type: ignore[typeddict-item]
    if "Style" in data:
        import aws_sdk_quicksight.types.geospatial_point_style

        out["style"] = aws_sdk_quicksight.types.geospatial_point_style.deserialize_json(
            data["Style"]
        )
    else:
        raise DeserializationError("GeospatialPointLayer.style required")
    return out
