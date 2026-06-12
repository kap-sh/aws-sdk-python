"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeSourceIdMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.uuid

AttributeSourceIdMap: TypeAlias = dict[
    "aws_sdk_customer_profiles.types.string1_to255.string1To255",
    "aws_sdk_customer_profiles.types.uuid.uuid",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AttributeSourceIdMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AttributeSourceIdMap:
    out: AttributeSourceIdMap = {}
    for key, value in data.items():
        out[key] = value
    return out
