"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ClientLocation``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_internetmonitor.errors import DeserializationError


class ClientLocation(TypedDict):
    as_name: "str"
    """<p>The name of the internet service provider (ISP) or network (ASN).</p>"""
    as_number: "int"
    """<p>The Autonomous System Number (ASN) of the network at an impacted location.</p>"""
    country: "str"
    """<p>The name of the country where the internet event is located.</p>"""
    subdivision: NotRequired["str"]
    """<p>The subdivision location where the health event is located. The subdivision usually maps to states in most countries (including the United States). For United Kingdom, it maps to a country (England, Scotland, Wales) or province (Northern Ireland).</p>"""
    metro: NotRequired["str"]
    """<p>The metro area where the health event is located.</p> <p>Metro indicates a metropolitan region in the United States, such as the region around New York City. In non-US countries, this is a second-level subdivision. For example, in the United Kingdom, it could be a county, a London borough, a unitary authority, council area, and so on.</p>"""
    city: "str"
    """<p>The name of the city where the internet event is located.</p>"""
    latitude: "float"
    """<p>The latitude where the internet event is located.</p>"""
    longitude: "float"
    """<p>The longitude where the internet event is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientLocation) -> dict:
    out: dict = {}
    out["ASName"] = value["as_name"]
    out["ASNumber"] = value["as_number"]
    out["Country"] = value["country"]
    if "subdivision" in value:
        out["Subdivision"] = value["subdivision"]
    if "metro" in value:
        out["Metro"] = value["metro"]
    out["City"] = value["city"]
    out["Latitude"] = value["latitude"]
    out["Longitude"] = value["longitude"]
    return out


def deserialize_json(data: dict) -> ClientLocation:
    out: ClientLocation = {}  # type: ignore[typeddict-item]
    if "ASName" in data:
        out["as_name"] = data["ASName"]
    else:
        raise DeserializationError("ClientLocation.as_name required")
    if "ASNumber" in data:
        out["as_number"] = data["ASNumber"]
    else:
        raise DeserializationError("ClientLocation.as_number required")
    if "Country" in data:
        out["country"] = data["Country"]
    else:
        raise DeserializationError("ClientLocation.country required")
    if "Subdivision" in data:
        out["subdivision"] = data["Subdivision"]
    if "Metro" in data:
        out["metro"] = data["Metro"]
    if "City" in data:
        out["city"] = data["City"]
    else:
        raise DeserializationError("ClientLocation.city required")
    if "Latitude" in data:
        out["latitude"] = data["Latitude"]
    else:
        raise DeserializationError("ClientLocation.latitude required")
    if "Longitude" in data:
        out["longitude"] = data["Longitude"]
    else:
        raise DeserializationError("ClientLocation.longitude required")
    return out
