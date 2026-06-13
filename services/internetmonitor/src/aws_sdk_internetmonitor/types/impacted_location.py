"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ImpactedLocation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.health_event_status
    import aws_sdk_internetmonitor.types.internet_health
    import aws_sdk_internetmonitor.types.ipv4_prefix_list
    import aws_sdk_internetmonitor.types.network_impairment


class ImpactedLocation(TypedDict):
    as_name: "str"
    """<p>The name of the internet service provider (ISP) or network (ASN).</p>"""
    as_number: "int"
    """<p>The Autonomous System Number (ASN) of the network at an impacted location.</p>"""
    country: "str"
    """<p>The name of the country where the health event is located.</p>"""
    subdivision: NotRequired["str"]
    """<p>The subdivision location where the health event is located. The subdivision usually maps to states in most countries (including the United States). For United Kingdom, it maps to a country (England, Scotland, Wales) or province (Northern Ireland).</p>"""
    metro: NotRequired["str"]
    """<p>The metro area where the health event is located.</p> <p>Metro indicates a metropolitan region in the United States, such as the region around New York City. In non-US countries, this is a second-level subdivision. For example, in the United Kingdom, it could be a county, a London borough, a unitary authority, council area, and so on.</p>"""
    city: NotRequired["str"]
    """<p>The name of the city where the health event is located.</p>"""
    latitude: NotRequired["float"]
    """<p>The latitude where the health event is located.</p>"""
    longitude: NotRequired["float"]
    """<p>The longitude where the health event is located.</p>"""
    country_code: NotRequired["str"]
    """<p>The country code where the health event is located. The ISO 3166-2 codes for the country is provided, when available. </p>"""
    subdivision_code: NotRequired["str"]
    """<p>The subdivision code where the health event is located. The ISO 3166-2 codes for country subdivisions is provided, when available. </p>"""
    service_location: NotRequired["str"]
    """<p>The service location where the health event is located.</p>"""
    status: "aws_sdk_internetmonitor.types.health_event_status.HealthEventStatus"
    """<p>The status of the health event at an impacted location.</p>"""
    caused_by: NotRequired[
        "aws_sdk_internetmonitor.types.network_impairment.NetworkImpairment"
    ]
    """<p>The cause of the impairment. There are two types of network impairments: Amazon Web Services network issues or internet issues. Internet issues are typically a problem with a network provider, like an internet service provider (ISP).</p>"""
    internet_health: NotRequired[
        "aws_sdk_internetmonitor.types.internet_health.InternetHealth"
    ]
    """<p>The calculated health at a specific location.</p>"""
    ipv4_prefixes: NotRequired[
        "aws_sdk_internetmonitor.types.ipv4_prefix_list.Ipv4PrefixList"
    ]
    """<p>The IPv4 prefixes at the client location that was impacted by the health event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImpactedLocation) -> dict:
    out: dict = {}
    out["ASName"] = value["as_name"]
    out["ASNumber"] = value["as_number"]
    out["Country"] = value["country"]
    if "subdivision" in value:
        out["Subdivision"] = value["subdivision"]
    if "metro" in value:
        out["Metro"] = value["metro"]
    if "city" in value:
        out["City"] = value["city"]
    if "latitude" in value:
        out["Latitude"] = value["latitude"]
    if "longitude" in value:
        out["Longitude"] = value["longitude"]
    if "country_code" in value:
        out["CountryCode"] = value["country_code"]
    if "subdivision_code" in value:
        out["SubdivisionCode"] = value["subdivision_code"]
    if "service_location" in value:
        out["ServiceLocation"] = value["service_location"]
    out["Status"] = value["status"]
    if "caused_by" in value:
        import aws_sdk_internetmonitor.types.network_impairment

        out["CausedBy"] = (
            aws_sdk_internetmonitor.types.network_impairment.serialize_json(
                value["caused_by"]
            )
        )
    if "internet_health" in value:
        import aws_sdk_internetmonitor.types.internet_health

        out["InternetHealth"] = (
            aws_sdk_internetmonitor.types.internet_health.serialize_json(
                value["internet_health"]
            )
        )
    if "ipv4_prefixes" in value:
        import aws_sdk_internetmonitor.types.ipv4_prefix_list

        out["Ipv4Prefixes"] = (
            aws_sdk_internetmonitor.types.ipv4_prefix_list.serialize_json(
                value["ipv4_prefixes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImpactedLocation:
    out: ImpactedLocation = {}  # type: ignore[typeddict-item]
    if "ASName" in data:
        out["as_name"] = data["ASName"]
    else:
        raise DeserializationError("ImpactedLocation.as_name required")
    if "ASNumber" in data:
        out["as_number"] = data["ASNumber"]
    else:
        raise DeserializationError("ImpactedLocation.as_number required")
    if "Country" in data:
        out["country"] = data["Country"]
    else:
        raise DeserializationError("ImpactedLocation.country required")
    if "Subdivision" in data:
        out["subdivision"] = data["Subdivision"]
    if "Metro" in data:
        out["metro"] = data["Metro"]
    if "City" in data:
        out["city"] = data["City"]
    if "Latitude" in data:
        out["latitude"] = data["Latitude"]
    if "Longitude" in data:
        out["longitude"] = data["Longitude"]
    if "CountryCode" in data:
        out["country_code"] = data["CountryCode"]
    if "SubdivisionCode" in data:
        out["subdivision_code"] = data["SubdivisionCode"]
    if "ServiceLocation" in data:
        out["service_location"] = data["ServiceLocation"]
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("ImpactedLocation.status required")
    if "CausedBy" in data:
        import aws_sdk_internetmonitor.types.network_impairment

        out["caused_by"] = (
            aws_sdk_internetmonitor.types.network_impairment.deserialize_json(
                data["CausedBy"]
            )
        )
    if "InternetHealth" in data:
        import aws_sdk_internetmonitor.types.internet_health

        out["internet_health"] = (
            aws_sdk_internetmonitor.types.internet_health.deserialize_json(
                data["InternetHealth"]
            )
        )
    if "Ipv4Prefixes" in data:
        import aws_sdk_internetmonitor.types.ipv4_prefix_list

        out["ipv4_prefixes"] = (
            aws_sdk_internetmonitor.types.ipv4_prefix_list.deserialize_json(
                data["Ipv4Prefixes"]
            )
        )
    return out
