"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialCircleRadius``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_radius


class GeospatialCircleRadius(TypedDict):
    radius: NotRequired["aws_sdk_quicksight.types.geospatial_radius.GeospatialRadius"]
    """<p>The positive value for the radius of a circle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialCircleRadius) -> dict:
    out: dict = {}
    if "radius" in value:
        out["Radius"] = value["radius"]
    return out


def deserialize_json(data: dict) -> GeospatialCircleRadius:
    out: GeospatialCircleRadius = {}  # type: ignore[typeddict-item]
    if "Radius" in data:
        out["radius"] = data["Radius"]
    return out
