"""Generated from Smithy shape ``com.amazonaws.securityhub#ActionRemoteIpDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.city
    import aws_sdk_securityhub.types.country
    import aws_sdk_securityhub.types.geo_location
    import aws_sdk_securityhub.types.ip_organization_details
    import aws_sdk_securityhub.types.non_empty_string


class ActionRemoteIpDetails(TypedDict, closed=True):
    ip_address_v4: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The IP address.</p>"""
    organization: NotRequired[
        "aws_sdk_securityhub.types.ip_organization_details.IpOrganizationDetails"
    ]
    """<p>The internet service provider (ISP) organization associated with the remote IP address.</p>"""
    country: NotRequired["aws_sdk_securityhub.types.country.Country"]
    """<p>The country where the remote IP address is located.</p>"""
    city: NotRequired["aws_sdk_securityhub.types.city.City"]
    """<p>The city where the remote IP address is located.</p>"""
    geo_location: NotRequired["aws_sdk_securityhub.types.geo_location.GeoLocation"]
    """<p>The coordinates of the location of the remote IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionRemoteIpDetails) -> dict:
    out: dict = {}
    if "ip_address_v4" in value:
        out["IpAddressV4"] = value["ip_address_v4"]
    if "organization" in value:
        import aws_sdk_securityhub.types.ip_organization_details

        out["Organization"] = (
            aws_sdk_securityhub.types.ip_organization_details.serialize_json(
                value["organization"]
            )
        )
    if "country" in value:
        import aws_sdk_securityhub.types.country

        out["Country"] = aws_sdk_securityhub.types.country.serialize_json(
            value["country"]
        )
    if "city" in value:
        import aws_sdk_securityhub.types.city

        out["City"] = aws_sdk_securityhub.types.city.serialize_json(value["city"])
    if "geo_location" in value:
        import aws_sdk_securityhub.types.geo_location

        out["GeoLocation"] = aws_sdk_securityhub.types.geo_location.serialize_json(
            value["geo_location"]
        )
    return out


def deserialize_json(data: dict) -> ActionRemoteIpDetails:
    out: ActionRemoteIpDetails = {}  # type: ignore[typeddict-item]
    if "IpAddressV4" in data:
        out["ip_address_v4"] = data["IpAddressV4"]
    if "Organization" in data:
        import aws_sdk_securityhub.types.ip_organization_details

        out["organization"] = (
            aws_sdk_securityhub.types.ip_organization_details.deserialize_json(
                data["Organization"]
            )
        )
    if "Country" in data:
        import aws_sdk_securityhub.types.country

        out["country"] = aws_sdk_securityhub.types.country.deserialize_json(
            data["Country"]
        )
    if "City" in data:
        import aws_sdk_securityhub.types.city

        out["city"] = aws_sdk_securityhub.types.city.deserialize_json(data["City"])
    if "GeoLocation" in data:
        import aws_sdk_securityhub.types.geo_location

        out["geo_location"] = aws_sdk_securityhub.types.geo_location.deserialize_json(
            data["GeoLocation"]
        )
    return out
