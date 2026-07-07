"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileTypeDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.profile_type_dimension_type
    import aws_sdk_customer_profiles.types.profile_type_values


class ProfileTypeDimension(TypedDict, closed=True):
    dimension_type: "aws_sdk_customer_profiles.types.profile_type_dimension_type.ProfileTypeDimensionType"
    """<p>The action to segment on.</p>"""
    values: "aws_sdk_customer_profiles.types.profile_type_values.ProfileTypeValues"
    """<p>The values to apply the DimensionType on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileTypeDimension) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.profile_type_dimension_type

    out["DimensionType"] = (
        aws_sdk_customer_profiles.types.profile_type_dimension_type.serialize_json(
            value["dimension_type"]
        )
    )
    import aws_sdk_customer_profiles.types.profile_type_values

    out["Values"] = aws_sdk_customer_profiles.types.profile_type_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> ProfileTypeDimension:
    out: ProfileTypeDimension = {}  # type: ignore[typeddict-item]
    if "DimensionType" in data:
        import aws_sdk_customer_profiles.types.profile_type_dimension_type

        out["dimension_type"] = (
            aws_sdk_customer_profiles.types.profile_type_dimension_type.deserialize_json(
                data["DimensionType"]
            )
        )
    else:
        raise DeserializationError("ProfileTypeDimension.dimension_type required")
    if "Values" in data:
        import aws_sdk_customer_profiles.types.profile_type_values

        out["values"] = (
            aws_sdk_customer_profiles.types.profile_type_values.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("ProfileTypeDimension.values required")
    return out
