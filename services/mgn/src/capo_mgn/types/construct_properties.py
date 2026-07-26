"""Generated from Smithy shape ``com.amazonaws.mgn#ConstructProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.construct_property_key
    import capo_mgn.types.marshalled_resource_definition

ConstructProperties: TypeAlias = dict[
    "capo_mgn.types.construct_property_key.ConstructPropertyKey",
    "capo_mgn.types.marshalled_resource_definition.MarshalledResourceDefinition",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConstructProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ConstructProperties:
    out: ConstructProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
