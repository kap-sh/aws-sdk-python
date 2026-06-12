"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Attributes``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_application_signals.types.key_attribute_name
    import aws_sdk_application_signals.types.key_attribute_value

Attributes: TypeAlias = dict["aws_sdk_application_signals.types.key_attribute_name.KeyAttributeName", "aws_sdk_application_signals.types.key_attribute_value.KeyAttributeValue"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Attributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Attributes:
    out: Attributes = {}
    for key, value in data.items():
        out[key] = value
    return out