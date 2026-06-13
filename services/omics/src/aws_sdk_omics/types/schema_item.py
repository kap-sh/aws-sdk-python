"""Generated from Smithy shape ``com.amazonaws.omics#SchemaItem``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.schema_value_type

SchemaItem: TypeAlias = dict[
    "str", "aws_sdk_omics.types.schema_value_type.SchemaValueType"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SchemaItem) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SchemaItem:
    out: SchemaItem = {}
    for key, value in data.items():
        out[key] = value
    return out
