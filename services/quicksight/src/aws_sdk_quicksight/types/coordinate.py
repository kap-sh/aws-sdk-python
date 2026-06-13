"""Generated from Smithy shape ``com.amazonaws.quicksight#Coordinate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.coordinate_latitude_double
    import aws_sdk_quicksight.types.coordinate_longitude_double


class Coordinate(TypedDict):
    latitude: (
        "aws_sdk_quicksight.types.coordinate_latitude_double.CoordinateLatitudeDouble"
    )
    """<p>The latitude coordinate value for the geocode preference.</p>"""
    longitude: (
        "aws_sdk_quicksight.types.coordinate_longitude_double.CoordinateLongitudeDouble"
    )
    """<p>The longitude coordinate value for the geocode preference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Coordinate) -> dict:
    out: dict = {}
    out["Latitude"] = value["latitude"]
    out["Longitude"] = value["longitude"]
    return out


def deserialize_json(data: dict) -> Coordinate:
    out: Coordinate = {}  # type: ignore[typeddict-item]
    if "Latitude" in data:
        out["latitude"] = data["Latitude"]
    else:
        raise DeserializationError("Coordinate.latitude required")
    if "Longitude" in data:
        out["longitude"] = data["Longitude"]
    else:
        raise DeserializationError("Coordinate.longitude required")
    return out
