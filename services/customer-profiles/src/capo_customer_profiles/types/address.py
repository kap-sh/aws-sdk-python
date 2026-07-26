"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Address``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to255


class Address(TypedDict, closed=True):
    address1: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The first line of a customer address.</p>"""
    address2: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The second line of a customer address.</p>"""
    address3: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The third line of a customer address.</p>"""
    address4: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The fourth line of a customer address.</p>"""
    city: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The city in which a customer lives.</p>"""
    county: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The county in which a customer lives.</p>"""
    state: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The state in which a customer lives.</p>"""
    province: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The province in which a customer lives.</p>"""
    country: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The country in which a customer lives.</p>"""
    postal_code: NotRequired["capo_customer_profiles.types.string1_to255.string1To255"]
    """<p>The postal code of a customer address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Address) -> dict:
    out: dict = {}
    if "address1" in value:
        out["Address1"] = value["address1"]
    if "address2" in value:
        out["Address2"] = value["address2"]
    if "address3" in value:
        out["Address3"] = value["address3"]
    if "address4" in value:
        out["Address4"] = value["address4"]
    if "city" in value:
        out["City"] = value["city"]
    if "county" in value:
        out["County"] = value["county"]
    if "state" in value:
        out["State"] = value["state"]
    if "province" in value:
        out["Province"] = value["province"]
    if "country" in value:
        out["Country"] = value["country"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    return out


def deserialize_json(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if "Address1" in data:
        out["address1"] = data["Address1"]
    if "Address2" in data:
        out["address2"] = data["Address2"]
    if "Address3" in data:
        out["address3"] = data["Address3"]
    if "Address4" in data:
        out["address4"] = data["Address4"]
    if "City" in data:
        out["city"] = data["City"]
    if "County" in data:
        out["county"] = data["County"]
    if "State" in data:
        out["state"] = data["State"]
    if "Province" in data:
        out["province"] = data["Province"]
    if "Country" in data:
        out["country"] = data["Country"]
    if "PostalCode" in data:
        out["postal_code"] = data["PostalCode"]
    return out
