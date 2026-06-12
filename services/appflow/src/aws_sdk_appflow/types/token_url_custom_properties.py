"""Generated from Smithy shape ``com.amazonaws.appflow#TokenUrlCustomProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.custom_property_key
    import aws_sdk_appflow.types.custom_property_value

TokenUrlCustomProperties: TypeAlias = dict[
    "aws_sdk_appflow.types.custom_property_key.CustomPropertyKey",
    "aws_sdk_appflow.types.custom_property_value.CustomPropertyValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TokenUrlCustomProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TokenUrlCustomProperties:
    out: TokenUrlCustomProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
