"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.gps_point_dimension
    import aws_sdk_pinpoint.types.set_dimension


class SegmentLocation(TypedDict):
    country: NotRequired["aws_sdk_pinpoint.types.set_dimension.SetDimension"]
    """<p>The country or region code, in ISO 3166-1 alpha-2 format, for the segment.</p>"""
    gps_point: NotRequired[
        "aws_sdk_pinpoint.types.gps_point_dimension.GPSPointDimension"
    ]
    """<p>The GPS location and range for the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentLocation) -> dict:
    out: dict = {}
    if "country" in value:
        import aws_sdk_pinpoint.types.set_dimension

        out["Country"] = aws_sdk_pinpoint.types.set_dimension.serialize_json(
            value["country"]
        )
    if "gps_point" in value:
        import aws_sdk_pinpoint.types.gps_point_dimension

        out["GPSPoint"] = aws_sdk_pinpoint.types.gps_point_dimension.serialize_json(
            value["gps_point"]
        )
    return out


def deserialize_json(data: dict) -> SegmentLocation:
    out: SegmentLocation = {}  # type: ignore[typeddict-item]
    if "Country" in data:
        import aws_sdk_pinpoint.types.set_dimension

        out["country"] = aws_sdk_pinpoint.types.set_dimension.deserialize_json(
            data["Country"]
        )
    if "GPSPoint" in data:
        import aws_sdk_pinpoint.types.gps_point_dimension

        out["gps_point"] = aws_sdk_pinpoint.types.gps_point_dimension.deserialize_json(
            data["GPSPoint"]
        )
    return out
