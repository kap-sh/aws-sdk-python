"""Generated from Smithy shape ``com.amazonaws.iot#ResourceAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.resource_attribute_key
    import capo_iot.types.resource_attribute_value

ResourceAttributes: TypeAlias = dict[
    "capo_iot.types.resource_attribute_key.ResourceAttributeKey",
    "capo_iot.types.resource_attribute_value.ResourceAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResourceAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ResourceAttributes:
    out: ResourceAttributes = {}
    for key, value in data.items():
        out[key] = value
    return out
