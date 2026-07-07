"""Generated from Smithy shape ``com.amazonaws.pinpoint#GPSPointDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__double
    import aws_sdk_pinpoint.types.gps_coordinates


class GPSPointDimension(TypedDict, closed=True):
    coordinates: NotRequired["aws_sdk_pinpoint.types.gps_coordinates.GPSCoordinates"]
    """<p>The GPS coordinates to measure distance from.</p>"""
    range_in_kilometers: NotRequired["aws_sdk_pinpoint.types.__double.__double"]
    """<p>The range, in kilometers, from the GPS coordinates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GPSPointDimension) -> dict:
    out: dict = {}
    if "coordinates" in value:
        import aws_sdk_pinpoint.types.gps_coordinates

        out["Coordinates"] = aws_sdk_pinpoint.types.gps_coordinates.serialize_json(
            value["coordinates"]
        )
    if "range_in_kilometers" in value:
        out["RangeInKilometers"] = value["range_in_kilometers"]
    return out


def deserialize_json(data: dict) -> GPSPointDimension:
    out: GPSPointDimension = {}  # type: ignore[typeddict-item]
    if "Coordinates" in data:
        import aws_sdk_pinpoint.types.gps_coordinates

        out["coordinates"] = aws_sdk_pinpoint.types.gps_coordinates.deserialize_json(
            data["Coordinates"]
        )
    if "RangeInKilometers" in data:
        out["range_in_kilometers"] = data["RangeInKilometers"]
    return out
