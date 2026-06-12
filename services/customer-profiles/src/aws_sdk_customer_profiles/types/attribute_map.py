"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.attribute_name
    import aws_sdk_customer_profiles.types.filter_attribute_dimension

AttributeMap: TypeAlias = dict[
    "aws_sdk_customer_profiles.types.attribute_name.attributeName",
    "aws_sdk_customer_profiles.types.filter_attribute_dimension.FilterAttributeDimension",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_customer_profiles.types.filter_attribute_dimension

        out[key] = (
            aws_sdk_customer_profiles.types.filter_attribute_dimension.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> AttributeMap:
    out: AttributeMap = {}
    for key, value in data.items():
        import aws_sdk_customer_profiles.types.filter_attribute_dimension

        out[key] = (
            aws_sdk_customer_profiles.types.filter_attribute_dimension.deserialize_json(
                value
            )
        )
    return out
