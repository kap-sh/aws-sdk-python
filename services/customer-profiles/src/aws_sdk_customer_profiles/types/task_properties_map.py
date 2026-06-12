"""Generated from Smithy shape ``com.amazonaws.customerprofiles#TaskPropertiesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.operator_properties_keys
    import aws_sdk_customer_profiles.types.property

TaskPropertiesMap: TypeAlias = dict[
    "aws_sdk_customer_profiles.types.operator_properties_keys.OperatorPropertiesKeys",
    "aws_sdk_customer_profiles.types.property.Property",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TaskPropertiesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_customer_profiles.types.operator_properties_keys

        out[
            aws_sdk_customer_profiles.types.operator_properties_keys.serialize_json(key)
        ] = value
    return out


def deserialize_json(data: dict) -> TaskPropertiesMap:
    out: TaskPropertiesMap = {}
    for key, value in data.items():
        import aws_sdk_customer_profiles.types.operator_properties_keys

        out[
            aws_sdk_customer_profiles.types.operator_properties_keys.deserialize_json(
                key
            )
        ] = value
    return out
