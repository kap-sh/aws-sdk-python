"""Generated from Smithy shape ``com.amazonaws.customerprofiles#KeyMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.object_type_key_list

KeyMap: TypeAlias = dict[
    "aws_sdk_customer_profiles.types.name.name",
    "aws_sdk_customer_profiles.types.object_type_key_list.ObjectTypeKeyList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: KeyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_customer_profiles.types.object_type_key_list

        out[key] = aws_sdk_customer_profiles.types.object_type_key_list.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> KeyMap:
    out: KeyMap = {}
    for key, value in data.items():
        import aws_sdk_customer_profiles.types.object_type_key_list

        out[key] = (
            aws_sdk_customer_profiles.types.object_type_key_list.deserialize_json(value)
        )
    return out
