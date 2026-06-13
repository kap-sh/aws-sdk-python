"""Generated from Smithy shape ``com.amazonaws.entityresolution#SchemaInputAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.schema_input_attribute

SchemaInputAttributes: TypeAlias = list[
    "aws_sdk_entityresolution.types.schema_input_attribute.SchemaInputAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: SchemaInputAttributes) -> list:
    import aws_sdk_entityresolution.types.schema_input_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.schema_input_attribute.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SchemaInputAttributes:
    import aws_sdk_entityresolution.types.schema_input_attribute

    out: SchemaInputAttributes = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.schema_input_attribute.deserialize_json(item)
        )
    return out
