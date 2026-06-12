"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CustomAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_dimension
    import aws_sdk_customer_profiles.types.string1_to255

CustomAttributes: TypeAlias = dict[
    "aws_sdk_customer_profiles.types.string1_to255.string1To255",
    "aws_sdk_customer_profiles.types.attribute_dimension.AttributeDimension",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CustomAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_customer_profiles.types.attribute_dimension

        out[key] = aws_sdk_customer_profiles.types.attribute_dimension.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> CustomAttributes:
    out: CustomAttributes = {}
    for key, value in data.items():
        import aws_sdk_customer_profiles.types.attribute_dimension

        out[key] = aws_sdk_customer_profiles.types.attribute_dimension.deserialize_json(
            value
        )
    return out
