"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkGeoLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.double
    import aws_sdk_guardduty.types.string


class NetworkGeoLocation(TypedDict, closed=True):
    city: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the city.</p>"""
    country: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the country.</p>"""
    latitude: NotRequired["aws_sdk_guardduty.types.double.Double"]
    """<p>The latitude information of the endpoint location.</p>"""
    longitude: NotRequired["aws_sdk_guardduty.types.double.Double"]
    """<p>The longitude information of the endpoint location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkGeoLocation) -> dict:
    out: dict = {}
    if "city" in value:
        out["city"] = value["city"]
    if "country" in value:
        out["country"] = value["country"]
    if "latitude" in value:
        out["lat"] = value["latitude"]
    if "longitude" in value:
        out["lon"] = value["longitude"]
    return out


def deserialize_json(data: dict) -> NetworkGeoLocation:
    out: NetworkGeoLocation = {}  # type: ignore[typeddict-item]
    if "city" in data:
        out["city"] = data["city"]
    if "country" in data:
        out["country"] = data["country"]
    if "lat" in data:
        out["latitude"] = data["lat"]
    if "lon" in data:
        out["longitude"] = data["lon"]
    return out
