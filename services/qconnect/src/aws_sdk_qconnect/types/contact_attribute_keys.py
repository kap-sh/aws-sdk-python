"""Generated from Smithy shape ``com.amazonaws.qconnect#ContactAttributeKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.contact_attribute_key

ContactAttributeKeys: TypeAlias = list[
    "aws_sdk_qconnect.types.contact_attribute_key.ContactAttributeKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactAttributeKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> ContactAttributeKeys:
    return list(data)
