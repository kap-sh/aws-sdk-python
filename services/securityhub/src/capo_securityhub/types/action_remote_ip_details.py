"""Generated from Smithy shape ``com.amazonaws.securityhub#ActionRemoteIpDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.city
    import capo_securityhub.types.country
    import capo_securityhub.types.geo_location
    import capo_securityhub.types.ip_organization_details
    import capo_securityhub.types.non_empty_string


class ActionRemoteIpDetails(TypedDict, closed=True):
    ip_address_v4: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The IP address.</p>"""
    organization: NotRequired[
        "capo_securityhub.types.ip_organization_details.IpOrganizationDetails"
    ]
    """<p>The internet service provider (ISP) organization associated with the remote IP address.</p>"""
    country: NotRequired["capo_securityhub.types.country.Country"]
    """<p>The country where the remote IP address is located.</p>"""
    city: NotRequired["capo_securityhub.types.city.City"]
    """<p>The city where the remote IP address is located.</p>"""
    geo_location: NotRequired["capo_securityhub.types.geo_location.GeoLocation"]
    """<p>The coordinates of the location of the remote IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionRemoteIpDetails) -> dict:
    out: dict = {}
    if "ip_address_v4" in value:
        out["IpAddressV4"] = value["ip_address_v4"]
    if "organization" in value:
        import capo_securityhub.types.ip_organization_details

        out["Organization"] = (
            capo_securityhub.types.ip_organization_details.serialize_json(
                value["organization"]
            )
        )
    if "country" in value:
        import capo_securityhub.types.country

        out["Country"] = capo_securityhub.types.country.serialize_json(value["country"])
    if "city" in value:
        import capo_securityhub.types.city

        out["City"] = capo_securityhub.types.city.serialize_json(value["city"])
    if "geo_location" in value:
        import capo_securityhub.types.geo_location

        out["GeoLocation"] = capo_securityhub.types.geo_location.serialize_json(
            value["geo_location"]
        )
    return out


def deserialize_json(data: dict) -> ActionRemoteIpDetails:
    out: ActionRemoteIpDetails = {}  # type: ignore[typeddict-item]
    if "IpAddressV4" in data:
        out["ip_address_v4"] = data["IpAddressV4"]
    if "Organization" in data:
        import capo_securityhub.types.ip_organization_details

        out["organization"] = (
            capo_securityhub.types.ip_organization_details.deserialize_json(
                data["Organization"]
            )
        )
    if "Country" in data:
        import capo_securityhub.types.country

        out["country"] = capo_securityhub.types.country.deserialize_json(
            data["Country"]
        )
    if "City" in data:
        import capo_securityhub.types.city

        out["city"] = capo_securityhub.types.city.deserialize_json(data["City"])
    if "GeoLocation" in data:
        import capo_securityhub.types.geo_location

        out["geo_location"] = capo_securityhub.types.geo_location.deserialize_json(
            data["GeoLocation"]
        )
    return out
