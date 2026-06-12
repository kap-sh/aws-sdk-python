"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FieldMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.field_name
    import aws_sdk_customer_profiles.types.object_type_field

FieldMap: TypeAlias = dict[
    "aws_sdk_customer_profiles.types.field_name.fieldName",
    "aws_sdk_customer_profiles.types.object_type_field.ObjectTypeField",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FieldMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_customer_profiles.types.object_type_field

        out[key] = aws_sdk_customer_profiles.types.object_type_field.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> FieldMap:
    out: FieldMap = {}
    for key, value in data.items():
        import aws_sdk_customer_profiles.types.object_type_field

        out[key] = aws_sdk_customer_profiles.types.object_type_field.deserialize_json(
            value
        )
    return out
