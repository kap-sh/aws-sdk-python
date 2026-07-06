"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Dimension``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.calculated_custom_attributes
    import aws_sdk_customer_profiles.types.profile_attributes


class _Dimension_ProfileAttributes(TypedDict, closed=True):
    ProfileAttributes: (
        "aws_sdk_customer_profiles.types.profile_attributes.ProfileAttributes"
    )


class _Dimension_CalculatedAttributes(TypedDict, closed=True):
    CalculatedAttributes: "aws_sdk_customer_profiles.types.calculated_custom_attributes.CalculatedCustomAttributes"


Dimension: TypeAlias = _Dimension_ProfileAttributes | _Dimension_CalculatedAttributes


# --- restJson1 ser/de ---
def serialize_json(value: Dimension) -> dict:
    if "ProfileAttributes" in value:
        import aws_sdk_customer_profiles.types.profile_attributes

        return {
            "ProfileAttributes": aws_sdk_customer_profiles.types.profile_attributes.serialize_json(
                value["ProfileAttributes"]
            )
        }
    elif "CalculatedAttributes" in value:
        import aws_sdk_customer_profiles.types.calculated_custom_attributes

        return {
            "CalculatedAttributes": aws_sdk_customer_profiles.types.calculated_custom_attributes.serialize_json(
                value["CalculatedAttributes"]
            )
        }
    else:
        raise SerializationError("Dimension: no variant present")


def deserialize_json(data: dict) -> Dimension:
    if "ProfileAttributes" in data:
        import aws_sdk_customer_profiles.types.profile_attributes

        return {
            "ProfileAttributes": aws_sdk_customer_profiles.types.profile_attributes.deserialize_json(
                data["ProfileAttributes"]
            )
        }
    elif "CalculatedAttributes" in data:
        import aws_sdk_customer_profiles.types.calculated_custom_attributes

        return {
            "CalculatedAttributes": aws_sdk_customer_profiles.types.calculated_custom_attributes.deserialize_json(
                data["CalculatedAttributes"]
            )
        }
    else:
        raise DeserializationError("Dimension: no recognized variant key")
