"""Generated from Smithy shape ``com.amazonaws.entityresolution#SchemaInputAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.schema_input_attribute

SchemaInputAttributes: TypeAlias = list[
    "capo_entityresolution.types.schema_input_attribute.SchemaInputAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaInputAttributes) -> list:
    import capo_entityresolution.types.schema_input_attribute

    out: list = []
    for item in value:
        out.append(
            capo_entityresolution.types.schema_input_attribute.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SchemaInputAttributes:
    import capo_entityresolution.types.schema_input_attribute

    out: SchemaInputAttributes = []
    for item in data:
        out.append(
            capo_entityresolution.types.schema_input_attribute.deserialize_json(item)
        )
    return out
