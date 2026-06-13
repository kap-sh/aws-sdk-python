"""Generated from Smithy shape ``com.amazonaws.invoicing#ReceiverAddress``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string


class ReceiverAddress(TypedDict):
    address_line1: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The first line of the address. </p>"""
    address_line2: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The second line of the address, if applicable. </p>"""
    address_line3: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The third line of the address, if applicable. </p>"""
    district_or_county: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The district or country the address is located in. </p>"""
    city: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The city that the address is in. </p>"""
    state_or_region: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The state, region, or province the address is located. </p>"""
    country_code: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The country code for the country the address is in. </p>"""
    company_name: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> A unique company name. </p>"""
    postal_code: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The postal code associated with the address. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReceiverAddress) -> dict:
    out: dict = {}
    if "address_line1" in value:
        out["AddressLine1"] = value["address_line1"]
    if "address_line2" in value:
        out["AddressLine2"] = value["address_line2"]
    if "address_line3" in value:
        out["AddressLine3"] = value["address_line3"]
    if "district_or_county" in value:
        out["DistrictOrCounty"] = value["district_or_county"]
    if "city" in value:
        out["City"] = value["city"]
    if "state_or_region" in value:
        out["StateOrRegion"] = value["state_or_region"]
    if "country_code" in value:
        out["CountryCode"] = value["country_code"]
    if "company_name" in value:
        out["CompanyName"] = value["company_name"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReceiverAddress:
    out: ReceiverAddress = {}  # type: ignore[typeddict-item]
    if "AddressLine1" in data:
        out["address_line1"] = data["AddressLine1"]
    if "AddressLine2" in data:
        out["address_line2"] = data["AddressLine2"]
    if "AddressLine3" in data:
        out["address_line3"] = data["AddressLine3"]
    if "DistrictOrCounty" in data:
        out["district_or_county"] = data["DistrictOrCounty"]
    if "City" in data:
        out["city"] = data["City"]
    if "StateOrRegion" in data:
        out["state_or_region"] = data["StateOrRegion"]
    if "CountryCode" in data:
        out["country_code"] = data["CountryCode"]
    if "CompanyName" in data:
        out["company_name"] = data["CompanyName"]
    if "PostalCode" in data:
        out["postal_code"] = data["PostalCode"]
    return out
