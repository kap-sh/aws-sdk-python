"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CalculatedCustomAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.calculated_attribute_dimension
    import aws_sdk_customer_profiles.types.type_name

CalculatedCustomAttributes: TypeAlias = dict[
    "aws_sdk_customer_profiles.types.type_name.typeName",
    "aws_sdk_customer_profiles.types.calculated_attribute_dimension.CalculatedAttributeDimension",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CalculatedCustomAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_customer_profiles.types.calculated_attribute_dimension

        out[key] = (
            aws_sdk_customer_profiles.types.calculated_attribute_dimension.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> CalculatedCustomAttributes:
    out: CalculatedCustomAttributes = {}
    for key, value in data.items():
        import aws_sdk_customer_profiles.types.calculated_attribute_dimension

        out[key] = (
            aws_sdk_customer_profiles.types.calculated_attribute_dimension.deserialize_json(
                value
            )
        )
    return out
