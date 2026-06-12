"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ObjectTypeNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.type_name

ObjectTypeNames: TypeAlias = dict[
    "aws_sdk_customer_profiles.types.string1_to255.string1To255",
    "aws_sdk_customer_profiles.types.type_name.typeName",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ObjectTypeNames) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ObjectTypeNames:
    out: ObjectTypeNames = {}
    for key, value in data.items():
        out[key] = value
    return out
