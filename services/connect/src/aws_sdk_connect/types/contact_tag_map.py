"""Generated from Smithy shape ``com.amazonaws.connect#ContactTagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_tag_key
    import aws_sdk_connect.types.contact_tag_value

ContactTagMap: TypeAlias = dict[
    "aws_sdk_connect.types.contact_tag_key.ContactTagKey",
    "aws_sdk_connect.types.contact_tag_value.ContactTagValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ContactTagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ContactTagMap:
    out: ContactTagMap = {}
    for key, value in data.items():
        out[key] = value
    return out
