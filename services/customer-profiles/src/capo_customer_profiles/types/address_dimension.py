"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AddressDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.profile_dimension


class AddressDimension(TypedDict, closed=True):
    city: NotRequired["capo_customer_profiles.types.profile_dimension.ProfileDimension"]
    """<p>The city belonging to the address.</p>"""
    country: NotRequired[
        "capo_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>The country belonging to the address.</p>"""
    county: NotRequired[
        "capo_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>The county belonging to the address.</p>"""
    postal_code: NotRequired[
        "capo_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>The postal code belonging to the address.</p>"""
    province: NotRequired[
        "capo_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>The province belonging to the address.</p>"""
    state: NotRequired[
        "capo_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>The state belonging to the address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddressDimension) -> dict:
    out: dict = {}
    if "city" in value:
        import capo_customer_profiles.types.profile_dimension

        out["City"] = capo_customer_profiles.types.profile_dimension.serialize_json(
            value["city"]
        )
    if "country" in value:
        import capo_customer_profiles.types.profile_dimension

        out["Country"] = capo_customer_profiles.types.profile_dimension.serialize_json(
            value["country"]
        )
    if "county" in value:
        import capo_customer_profiles.types.profile_dimension

        out["County"] = capo_customer_profiles.types.profile_dimension.serialize_json(
            value["county"]
        )
    if "postal_code" in value:
        import capo_customer_profiles.types.profile_dimension

        out["PostalCode"] = (
            capo_customer_profiles.types.profile_dimension.serialize_json(
                value["postal_code"]
            )
        )
    if "province" in value:
        import capo_customer_profiles.types.profile_dimension

        out["Province"] = capo_customer_profiles.types.profile_dimension.serialize_json(
            value["province"]
        )
    if "state" in value:
        import capo_customer_profiles.types.profile_dimension

        out["State"] = capo_customer_profiles.types.profile_dimension.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> AddressDimension:
    out: AddressDimension = {}  # type: ignore[typeddict-item]
    if "City" in data:
        import capo_customer_profiles.types.profile_dimension

        out["city"] = capo_customer_profiles.types.profile_dimension.deserialize_json(
            data["City"]
        )
    if "Country" in data:
        import capo_customer_profiles.types.profile_dimension

        out["country"] = (
            capo_customer_profiles.types.profile_dimension.deserialize_json(
                data["Country"]
            )
        )
    if "County" in data:
        import capo_customer_profiles.types.profile_dimension

        out["county"] = capo_customer_profiles.types.profile_dimension.deserialize_json(
            data["County"]
        )
    if "PostalCode" in data:
        import capo_customer_profiles.types.profile_dimension

        out["postal_code"] = (
            capo_customer_profiles.types.profile_dimension.deserialize_json(
                data["PostalCode"]
            )
        )
    if "Province" in data:
        import capo_customer_profiles.types.profile_dimension

        out["province"] = (
            capo_customer_profiles.types.profile_dimension.deserialize_json(
                data["Province"]
            )
        )
    if "State" in data:
        import capo_customer_profiles.types.profile_dimension

        out["state"] = capo_customer_profiles.types.profile_dimension.deserialize_json(
            data["State"]
        )
    return out
