"""Generated from Smithy shape ``com.amazonaws.location#TrackingFilterGeometry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_location.types.linear_rings


class TrackingFilterGeometry(TypedDict):
    polygon: NotRequired["aws_sdk_location.types.linear_rings.LinearRings"]
    """<p>The set of arrays which define the polygon. A polygon can have between 4 and 1000 vertices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrackingFilterGeometry) -> dict:
    out: dict = {}
    if "polygon" in value:
        import aws_sdk_location.types.linear_rings

        out["Polygon"] = aws_sdk_location.types.linear_rings.serialize_json(
            value["polygon"]
        )
    return out


def deserialize_json(data: dict) -> TrackingFilterGeometry:
    out: TrackingFilterGeometry = {}  # type: ignore[typeddict-item]
    if "Polygon" in data:
        import aws_sdk_location.types.linear_rings

        out["polygon"] = aws_sdk_location.types.linear_rings.deserialize_json(
            data["Polygon"]
        )
    return out
