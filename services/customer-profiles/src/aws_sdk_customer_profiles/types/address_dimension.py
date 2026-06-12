"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AddressDimension``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.profile_dimension


class AddressDimension(TypedDict):
    city: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>The city belonging to the address.</p>"""
    country: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>The country belonging to the address.</p>"""
    county: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>The county belonging to the address.</p>"""
    postal_code: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>The postal code belonging to the address.</p>"""
    province: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>The province belonging to the address.</p>"""
    state: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>The state belonging to the address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddressDimension) -> dict:
    out: dict = {}
    if "city" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["City"] = aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
            value["city"]
        )
    if "country" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["Country"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["country"]
            )
        )
    if "county" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["County"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["county"]
            )
        )
    if "postal_code" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["PostalCode"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["postal_code"]
            )
        )
    if "province" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["Province"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["province"]
            )
        )
    if "state" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["State"] = aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> AddressDimension:
    out: AddressDimension = {}  # type: ignore[typeddict-item]
    if "City" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["city"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["City"]
            )
        )
    if "Country" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["country"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["Country"]
            )
        )
    if "County" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["county"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["County"]
            )
        )
    if "PostalCode" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["postal_code"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["PostalCode"]
            )
        )
    if "Province" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["province"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["Province"]
            )
        )
    if "State" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["state"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["State"]
            )
        )
    return out
