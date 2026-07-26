"""Generated from Smithy shape ``com.amazonaws.iot#Attributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.attribute_name
    import capo_iot.types.attribute_value

Attributes: TypeAlias = dict[
    "capo_iot.types.attribute_name.AttributeName",
    "capo_iot.types.attribute_value.AttributeValue",
]


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
