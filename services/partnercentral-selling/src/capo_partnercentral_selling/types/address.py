"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Address``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.address_part
    import capo_partnercentral_selling.types.country_code


class Address(TypedDict, closed=True):
    city: NotRequired["capo_partnercentral_selling.types.address_part.AddressPart"]
    """<p>Specifies the end <code>Customer</code>'s city associated with the <code>Opportunity</code>.</p>"""
    postal_code: NotRequired[
        "capo_partnercentral_selling.types.address_part.AddressPart"
    ]
    """<p>Specifies the end <code>Customer</code>'s postal code associated with the <code>Opportunity</code>.</p>"""
    state_or_region: NotRequired[
        "capo_partnercentral_selling.types.address_part.AddressPart"
    ]
    """<p>Specifies the end <code>Customer</code>'s state or region associated with the <code>Opportunity</code>.</p> <p>Valid values: <code>Alabama | Alaska | American Samoa | Arizona | Arkansas | California | Colorado | Connecticut | Delaware | Dist. of Columbia | Federated States of Micronesia | Florida | Georgia | Guam | Hawaii | Idaho | Illinois | Indiana | Iowa | Kansas | Kentucky | Louisiana | Maine | Marshall Islands | Maryland | Massachusetts | Michigan | Minnesota | Mississippi | Missouri | Montana | Nebraska | Nevada | New Hampshire | New Jersey | New Mexico | New York | North Carolina | North Dakota | Northern Mariana Islands | Ohio | Oklahoma | Oregon | Palau | Pennsylvania | Puerto Rico | Rhode Island | South Carolina | South Dakota | Tennessee | Texas | Utah | Vermont | Virginia | Virgin Islands | Washington | West Virginia | Wisconsin | Wyoming | APO/AE | AFO/FPO | FPO, AP</code> </p>"""
    country_code: NotRequired[
        "capo_partnercentral_selling.types.country_code.CountryCode"
    ]
    """<p>Specifies the end <code>Customer</code>'s country associated with the <code>Opportunity</code>.</p>"""
    street_address: NotRequired[
        "capo_partnercentral_selling.types.address_part.AddressPart"
    ]
    """<p>Specifies the end <code>Customer</code>'s street address associated with the <code>Opportunity</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Address) -> dict:
    out: dict = {}
    if "city" in value:
        out["City"] = value["city"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "state_or_region" in value:
        out["StateOrRegion"] = value["state_or_region"]
    if "country_code" in value:
        import capo_partnercentral_selling.types.country_code

        out["CountryCode"] = (
            capo_partnercentral_selling.types.country_code.serialize_aws_json_1_0(
                value["country_code"]
            )
        )
    if "street_address" in value:
        out["StreetAddress"] = value["street_address"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if "City" in data:
        out["city"] = data["City"]
    if "PostalCode" in data:
        out["postal_code"] = data["PostalCode"]
    if "StateOrRegion" in data:
        out["state_or_region"] = data["StateOrRegion"]
    if "CountryCode" in data:
        import capo_partnercentral_selling.types.country_code

        out["country_code"] = (
            capo_partnercentral_selling.types.country_code.deserialize_aws_json_1_0(
                data["CountryCode"]
            )
        )
    if "StreetAddress" in data:
        out["street_address"] = data["StreetAddress"]
    return out
