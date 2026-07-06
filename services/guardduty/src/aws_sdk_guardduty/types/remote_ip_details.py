"""Generated from Smithy shape ``com.amazonaws.guardduty#RemoteIpDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.city
    import aws_sdk_guardduty.types.country
    import aws_sdk_guardduty.types.geo_location
    import aws_sdk_guardduty.types.organization
    import aws_sdk_guardduty.types.sensitive_string


class RemoteIpDetails(TypedDict, closed=True):
    city: NotRequired["aws_sdk_guardduty.types.city.City"]
    """<p>The city information of the remote IP address.</p>"""
    country: NotRequired["aws_sdk_guardduty.types.country.Country"]
    """<p>The country code of the remote IP address.</p>"""
    geo_location: NotRequired["aws_sdk_guardduty.types.geo_location.GeoLocation"]
    """<p>The location information of the remote IP address.</p>"""
    ip_address_v4: NotRequired[
        "aws_sdk_guardduty.types.sensitive_string.SensitiveString"
    ]
    """<p>The IPv4 remote address of the connection.</p>"""
    ip_address_v6: NotRequired[
        "aws_sdk_guardduty.types.sensitive_string.SensitiveString"
    ]
    """<p>The IPv6 remote address of the connection.</p>"""
    organization: NotRequired["aws_sdk_guardduty.types.organization.Organization"]
    """<p>The ISP organization information of the remote IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteIpDetails) -> dict:
    out: dict = {}
    if "city" in value:
        import aws_sdk_guardduty.types.city

        out["city"] = aws_sdk_guardduty.types.city.serialize_json(value["city"])
    if "country" in value:
        import aws_sdk_guardduty.types.country

        out["country"] = aws_sdk_guardduty.types.country.serialize_json(
            value["country"]
        )
    if "geo_location" in value:
        import aws_sdk_guardduty.types.geo_location

        out["geoLocation"] = aws_sdk_guardduty.types.geo_location.serialize_json(
            value["geo_location"]
        )
    if "ip_address_v4" in value:
        out["ipAddressV4"] = value["ip_address_v4"]
    if "ip_address_v6" in value:
        out["ipAddressV6"] = value["ip_address_v6"]
    if "organization" in value:
        import aws_sdk_guardduty.types.organization

        out["organization"] = aws_sdk_guardduty.types.organization.serialize_json(
            value["organization"]
        )
    return out


def deserialize_json(data: dict) -> RemoteIpDetails:
    out: RemoteIpDetails = {}  # type: ignore[typeddict-item]
    if "city" in data:
        import aws_sdk_guardduty.types.city

        out["city"] = aws_sdk_guardduty.types.city.deserialize_json(data["city"])
    if "country" in data:
        import aws_sdk_guardduty.types.country

        out["country"] = aws_sdk_guardduty.types.country.deserialize_json(
            data["country"]
        )
    if "geoLocation" in data:
        import aws_sdk_guardduty.types.geo_location

        out["geo_location"] = aws_sdk_guardduty.types.geo_location.deserialize_json(
            data["geoLocation"]
        )
    if "ipAddressV4" in data:
        out["ip_address_v4"] = data["ipAddressV4"]
    if "ipAddressV6" in data:
        out["ip_address_v6"] = data["ipAddressV6"]
    if "organization" in data:
        import aws_sdk_guardduty.types.organization

        out["organization"] = aws_sdk_guardduty.types.organization.deserialize_json(
            data["organization"]
        )
    return out
