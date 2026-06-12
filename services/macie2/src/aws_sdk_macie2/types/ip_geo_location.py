"""Generated from Smithy shape ``com.amazonaws.macie2#IpGeoLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__double


class IpGeoLocation(TypedDict):
    lat: NotRequired["aws_sdk_macie2.types.__double.__double"]
    """<p>The latitude coordinate of the location, rounded to four decimal places.</p>"""
    lon: NotRequired["aws_sdk_macie2.types.__double.__double"]
    """<p>The longitude coordinate of the location, rounded to four decimal places.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpGeoLocation) -> dict:
    out: dict = {}
    if "lat" in value:
        out["lat"] = value["lat"]
    if "lon" in value:
        out["lon"] = value["lon"]
    return out


def deserialize_json(data: dict) -> IpGeoLocation:
    out: IpGeoLocation = {}  # type: ignore[typeddict-item]
    if "lat" in data:
        out["lat"] = data["lat"]
    if "lon" in data:
        out["lon"] = data["lon"]
    return out
