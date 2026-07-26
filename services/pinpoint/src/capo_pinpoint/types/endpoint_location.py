"""Generated from Smithy shape ``com.amazonaws.pinpoint#EndpointLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__double
    import capo_pinpoint.types.__string


class EndpointLocation(TypedDict, closed=True):
    city: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the city where the endpoint is located.</p>"""
    country: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The two-character code, in ISO 3166-1 alpha-2 format, for the country or region where the endpoint is located. For example, US for the United States.</p>"""
    latitude: NotRequired["capo_pinpoint.types.__double.__double"]
    """<p>The latitude coordinate of the endpoint location, rounded to one decimal place.</p>"""
    longitude: NotRequired["capo_pinpoint.types.__double.__double"]
    """<p>The longitude coordinate of the endpoint location, rounded to one decimal place.</p>"""
    postal_code: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The postal or ZIP code for the area where the endpoint is located.</p>"""
    region: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the region where the endpoint is located. For locations in the United States, this value is the name of a state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointLocation) -> dict:
    out: dict = {}
    if "city" in value:
        out["City"] = value["city"]
    if "country" in value:
        out["Country"] = value["country"]
    if "latitude" in value:
        out["Latitude"] = value["latitude"]
    if "longitude" in value:
        out["Longitude"] = value["longitude"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> EndpointLocation:
    out: EndpointLocation = {}  # type: ignore[typeddict-item]
    if "City" in data:
        out["city"] = data["City"]
    if "Country" in data:
        out["country"] = data["Country"]
    if "Latitude" in data:
        out["latitude"] = data["Latitude"]
    if "Longitude" in data:
        out["longitude"] = data["Longitude"]
    if "PostalCode" in data:
        out["postal_code"] = data["PostalCode"]
    if "Region" in data:
        out["region"] = data["Region"]
    return out
