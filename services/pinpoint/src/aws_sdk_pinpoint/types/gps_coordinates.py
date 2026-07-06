"""Generated from Smithy shape ``com.amazonaws.pinpoint#GPSCoordinates``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__double


class GPSCoordinates(TypedDict, closed=True):
    latitude: NotRequired["aws_sdk_pinpoint.types.__double.__double"]
    """<p>The latitude coordinate of the location.</p>"""
    longitude: NotRequired["aws_sdk_pinpoint.types.__double.__double"]
    """<p>The longitude coordinate of the location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GPSCoordinates) -> dict:
    out: dict = {}
    if "latitude" in value:
        out["Latitude"] = value["latitude"]
    if "longitude" in value:
        out["Longitude"] = value["longitude"]
    return out


def deserialize_json(data: dict) -> GPSCoordinates:
    out: GPSCoordinates = {}  # type: ignore[typeddict-item]
    if "Latitude" in data:
        out["latitude"] = data["Latitude"]
    if "Longitude" in data:
        out["longitude"] = data["Longitude"]
    return out
