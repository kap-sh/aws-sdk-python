"""Generated from Smithy shape ``com.amazonaws.securityhub#GeoLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.double


class GeoLocation(TypedDict):
    lon: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p>The longitude of the location.</p>"""
    lat: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p>The latitude of the location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeoLocation) -> dict:
    out: dict = {}
    if "lon" in value:
        out["Lon"] = value["lon"]
    if "lat" in value:
        out["Lat"] = value["lat"]
    return out


def deserialize_json(data: dict) -> GeoLocation:
    out: GeoLocation = {}  # type: ignore[typeddict-item]
    if "Lon" in data:
        out["lon"] = data["Lon"]
    if "Lat" in data:
        out["lat"] = data["Lat"]
    return out
