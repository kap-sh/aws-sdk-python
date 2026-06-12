"""Generated from Smithy shape ``com.amazonaws.account#ContactInformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_account.types.address_line
    import aws_sdk_account.types.city
    import aws_sdk_account.types.company_name
    import aws_sdk_account.types.contact_information_phone_number
    import aws_sdk_account.types.country_code
    import aws_sdk_account.types.district_or_county
    import aws_sdk_account.types.full_name
    import aws_sdk_account.types.postal_code
    import aws_sdk_account.types.state_or_region
    import aws_sdk_account.types.website_url


class ContactInformation(TypedDict):
    full_name: "aws_sdk_account.types.full_name.FullName"
    """<p>The full name of the primary contact address.</p>"""
    address_line1: "aws_sdk_account.types.address_line.AddressLine"
    """<p>The first line of the primary contact address.</p>"""
    address_line2: NotRequired["aws_sdk_account.types.address_line.AddressLine"]
    """<p>The second line of the primary contact address, if any.</p>"""
    address_line3: NotRequired["aws_sdk_account.types.address_line.AddressLine"]
    """<p>The third line of the primary contact address, if any.</p>"""
    city: "aws_sdk_account.types.city.City"
    """<p>The city of the primary contact address.</p>"""
    state_or_region: NotRequired["aws_sdk_account.types.state_or_region.StateOrRegion"]
    """<p>The state or region of the primary contact address. If the mailing address is within the United States (US), the value in this field can be either a two character state code (for example, <code>NJ</code>) or the full state name (for example, <code>New Jersey</code>). This field is required in the following countries: <code>US</code>, <code>CA</code>, <code>GB</code>, <code>DE</code>, <code>JP</code>, <code>IN</code>, and <code>BR</code>.</p>"""
    district_or_county: NotRequired[
        "aws_sdk_account.types.district_or_county.DistrictOrCounty"
    ]
    """<p>The district or county of the primary contact address, if any.</p>"""
    postal_code: "aws_sdk_account.types.postal_code.PostalCode"
    """<p>The postal code of the primary contact address.</p>"""
    country_code: "aws_sdk_account.types.country_code.CountryCode"
    """<p>The ISO-3166 two-letter country code for the primary contact address.</p>"""
    phone_number: "aws_sdk_account.types.contact_information_phone_number.ContactInformationPhoneNumber"
    """<p>The phone number of the primary contact information. The number will be validated and, in some countries, checked for activation.</p>"""
    company_name: NotRequired["aws_sdk_account.types.company_name.CompanyName"]
    """<p>The name of the company associated with the primary contact information, if any.</p>"""
    website_url: NotRequired["aws_sdk_account.types.website_url.WebsiteUrl"]
    """<p>The URL of the website associated with the primary contact information, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactInformation) -> dict:
    out: dict = {}
    out["FullName"] = value["full_name"]
    out["AddressLine1"] = value["address_line1"]
    if "address_line2" in value:
        out["AddressLine2"] = value["address_line2"]
    if "address_line3" in value:
        out["AddressLine3"] = value["address_line3"]
    out["City"] = value["city"]
    if "state_or_region" in value:
        out["StateOrRegion"] = value["state_or_region"]
    if "district_or_county" in value:
        out["DistrictOrCounty"] = value["district_or_county"]
    out["PostalCode"] = value["postal_code"]
    out["CountryCode"] = value["country_code"]
    out["PhoneNumber"] = value["phone_number"]
    if "company_name" in value:
        out["CompanyName"] = value["company_name"]
    if "website_url" in value:
        out["WebsiteUrl"] = value["website_url"]
    return out


def deserialize_json(data: dict) -> ContactInformation:
    out: ContactInformation = {}  # type: ignore[typeddict-item]
    if "FullName" in data:
        out["full_name"] = data["FullName"]
    else:
        raise DeserializationError("ContactInformation.full_name required")
    if "AddressLine1" in data:
        out["address_line1"] = data["AddressLine1"]
    else:
        raise DeserializationError("ContactInformation.address_line1 required")
    if "AddressLine2" in data:
        out["address_line2"] = data["AddressLine2"]
    if "AddressLine3" in data:
        out["address_line3"] = data["AddressLine3"]
    if "City" in data:
        out["city"] = data["City"]
    else:
        raise DeserializationError("ContactInformation.city required")
    if "StateOrRegion" in data:
        out["state_or_region"] = data["StateOrRegion"]
    if "DistrictOrCounty" in data:
        out["district_or_county"] = data["DistrictOrCounty"]
    if "PostalCode" in data:
        out["postal_code"] = data["PostalCode"]
    else:
        raise DeserializationError("ContactInformation.postal_code required")
    if "CountryCode" in data:
        out["country_code"] = data["CountryCode"]
    else:
        raise DeserializationError("ContactInformation.country_code required")
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    else:
        raise DeserializationError("ContactInformation.phone_number required")
    if "CompanyName" in data:
        out["company_name"] = data["CompanyName"]
    if "WebsiteUrl" in data:
        out["website_url"] = data["WebsiteUrl"]
    return out
