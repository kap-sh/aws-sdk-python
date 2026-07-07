"""Generated from Smithy shape ``com.amazonaws.guardduty#GeoLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.double


class GeoLocation(TypedDict, closed=True):
    lat: NotRequired["aws_sdk_guardduty.types.double.Double"]
    """<p>The latitude information of the remote IP address.</p>"""
    lon: NotRequired["aws_sdk_guardduty.types.double.Double"]
    """<p>The longitude information of the remote IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeoLocation) -> dict:
    out: dict = {}
    if "lat" in value:
        out["lat"] = value["lat"]
    if "lon" in value:
        out["lon"] = value["lon"]
    return out


def deserialize_json(data: dict) -> GeoLocation:
    out: GeoLocation = {}  # type: ignore[typeddict-item]
    if "lat" in data:
        out["lat"] = data["lat"]
    if "lon" in data:
        out["lon"] = data["lon"]
    return out
