"""Generated from Smithy shape ``com.amazonaws.macie2#IpAddressDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.ip_city
    import capo_macie2.types.ip_country
    import capo_macie2.types.ip_geo_location
    import capo_macie2.types.ip_owner


class IpAddressDetails(TypedDict, closed=True):
    ip_address_v4: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Internet Protocol version 4 (IPv4) address of the device.</p>"""
    ip_city: NotRequired["capo_macie2.types.ip_city.IpCity"]
    """<p>The city that the IP address originated from.</p>"""
    ip_country: NotRequired["capo_macie2.types.ip_country.IpCountry"]
    """<p>The country that the IP address originated from.</p>"""
    ip_geo_location: NotRequired["capo_macie2.types.ip_geo_location.IpGeoLocation"]
    """<p>The geographic coordinates of the location that the IP address originated from.</p>"""
    ip_owner: NotRequired["capo_macie2.types.ip_owner.IpOwner"]
    """<p>The registered owner of the IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpAddressDetails) -> dict:
    out: dict = {}
    if "ip_address_v4" in value:
        out["ipAddressV4"] = value["ip_address_v4"]
    if "ip_city" in value:
        import capo_macie2.types.ip_city

        out["ipCity"] = capo_macie2.types.ip_city.serialize_json(value["ip_city"])
    if "ip_country" in value:
        import capo_macie2.types.ip_country

        out["ipCountry"] = capo_macie2.types.ip_country.serialize_json(
            value["ip_country"]
        )
    if "ip_geo_location" in value:
        import capo_macie2.types.ip_geo_location

        out["ipGeoLocation"] = capo_macie2.types.ip_geo_location.serialize_json(
            value["ip_geo_location"]
        )
    if "ip_owner" in value:
        import capo_macie2.types.ip_owner

        out["ipOwner"] = capo_macie2.types.ip_owner.serialize_json(value["ip_owner"])
    return out


def deserialize_json(data: dict) -> IpAddressDetails:
    out: IpAddressDetails = {}  # type: ignore[typeddict-item]
    if "ipAddressV4" in data:
        out["ip_address_v4"] = data["ipAddressV4"]
    if "ipCity" in data:
        import capo_macie2.types.ip_city

        out["ip_city"] = capo_macie2.types.ip_city.deserialize_json(data["ipCity"])
    if "ipCountry" in data:
        import capo_macie2.types.ip_country

        out["ip_country"] = capo_macie2.types.ip_country.deserialize_json(
            data["ipCountry"]
        )
    if "ipGeoLocation" in data:
        import capo_macie2.types.ip_geo_location

        out["ip_geo_location"] = capo_macie2.types.ip_geo_location.deserialize_json(
            data["ipGeoLocation"]
        )
    if "ipOwner" in data:
        import capo_macie2.types.ip_owner

        out["ip_owner"] = capo_macie2.types.ip_owner.deserialize_json(data["ipOwner"])
    return out
