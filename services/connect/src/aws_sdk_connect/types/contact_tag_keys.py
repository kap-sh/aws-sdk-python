"""Generated from Smithy shape ``com.amazonaws.connect#ContactTagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_tag_key

ContactTagKeys: TypeAlias = list["aws_sdk_connect.types.contact_tag_key.ContactTagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: ContactTagKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> ContactTagKeys:
    return list(data)
