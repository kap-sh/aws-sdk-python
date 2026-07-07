"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkGeoLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.double
    import aws_sdk_securityhub.types.non_empty_string


class NetworkGeoLocation(TypedDict, closed=True):
    city: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the city. </p>"""
    country: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the country. </p>"""
    lat: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p> The latitude information of the endpoint location. </p>"""
    lon: NotRequired["aws_sdk_securityhub.types.double.Double"]
    """<p> The longitude information of the endpoint location. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkGeoLocation) -> dict:
    out: dict = {}
    if "city" in value:
        out["City"] = value["city"]
    if "country" in value:
        out["Country"] = value["country"]
    if "lat" in value:
        out["Lat"] = value["lat"]
    if "lon" in value:
        out["Lon"] = value["lon"]
    return out


def deserialize_json(data: dict) -> NetworkGeoLocation:
    out: NetworkGeoLocation = {}  # type: ignore[typeddict-item]
    if "City" in data:
        out["city"] = data["City"]
    if "Country" in data:
        out["country"] = data["Country"]
    if "Lat" in data:
        out["lat"] = data["Lat"]
    if "Lon" in data:
        out["lon"] = data["Lon"]
    return out
