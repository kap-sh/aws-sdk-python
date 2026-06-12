"""Generated from Smithy shape ``com.amazonaws.finspace#AttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.federation_attribute_key
    import aws_sdk_finspace.types.federation_attribute_value

AttributeMap: TypeAlias = dict[
    "aws_sdk_finspace.types.federation_attribute_key.FederationAttributeKey",
    "aws_sdk_finspace.types.federation_attribute_value.FederationAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AttributeMap:
    out: AttributeMap = {}
    for key, value in data.items():
        out[key] = value
    return out
