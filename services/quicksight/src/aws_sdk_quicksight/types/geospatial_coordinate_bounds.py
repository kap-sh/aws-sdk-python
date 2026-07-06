"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialCoordinateBounds``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.latitude
    import aws_sdk_quicksight.types.longitude


class GeospatialCoordinateBounds(TypedDict, closed=True):
    north: "aws_sdk_quicksight.types.latitude.Latitude"
    """<p>The latitude of the north bound of the geospatial coordinate bounds.</p>"""
    south: "aws_sdk_quicksight.types.latitude.Latitude"
    """<p>The latitude of the south bound of the geospatial coordinate bounds.</p>"""
    west: "aws_sdk_quicksight.types.longitude.Longitude"
    """<p>The longitude of the west bound of the geospatial coordinate bounds.</p>"""
    east: "aws_sdk_quicksight.types.longitude.Longitude"
    """<p>The longitude of the east bound of the geospatial coordinate bounds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialCoordinateBounds) -> dict:
    out: dict = {}
    out["North"] = value["north"]
    out["South"] = value["south"]
    out["West"] = value["west"]
    out["East"] = value["east"]
    return out


def deserialize_json(data: dict) -> GeospatialCoordinateBounds:
    out: GeospatialCoordinateBounds = {}  # type: ignore[typeddict-item]
    if "North" in data:
        out["north"] = data["North"]
    else:
        raise DeserializationError("GeospatialCoordinateBounds.north required")
    if "South" in data:
        out["south"] = data["South"]
    else:
        raise DeserializationError("GeospatialCoordinateBounds.south required")
    if "West" in data:
        out["west"] = data["West"]
    else:
        raise DeserializationError("GeospatialCoordinateBounds.west required")
    if "East" in data:
        out["east"] = data["East"]
    else:
        raise DeserializationError("GeospatialCoordinateBounds.east required")
    return out
