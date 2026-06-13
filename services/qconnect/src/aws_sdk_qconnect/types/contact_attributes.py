"""Generated from Smithy shape ``com.amazonaws.qconnect#ContactAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.contact_attribute_key
    import aws_sdk_qconnect.types.contact_attribute_value

ContactAttributes: TypeAlias = dict[
    "aws_sdk_qconnect.types.contact_attribute_key.ContactAttributeKey",
    "aws_sdk_qconnect.types.contact_attribute_value.ContactAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ContactAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ContactAttributes:
    out: ContactAttributes = {}
    for key, value in data.items():
        out[key] = value
    return out
